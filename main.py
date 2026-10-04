import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from agents.restaurant_finder import restaurant_finder_agent


def text_from_content(content):
    if isinstance(content, str):
        return content
    if isinstance(content, dict):
        return content.get("text", "")
    if isinstance(content, list):
        return "".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    return ""


def message_role(message):
    if isinstance(message, dict):
        return message.get("role")
    role = getattr(message, "type", None)
    if role == "human":
        return "user"
    if role == "ai":
        return "assistant"
    return None


st.set_page_config(page_title="Restaurant Finder", page_icon="🍽️")
st.title("Restaurant Finder")

st.session_state.setdefault("conversation", [])

if st.button("Nowe zapytanie", icon="➕"):
    st.session_state.conversation = []
    st.rerun()

st.caption("Zapytaj o restaurację, poproś o rezerwację albo odpowiedz na pytanie agenta.")

for message in st.session_state.conversation:
    role = message_role(message)
    content = text_from_content(
        message.get("content", "") if isinstance(message, dict) else getattr(message, "content", "")
    )
    if role and content:
        with st.chat_message(role):
            st.markdown(content)

user_request = st.chat_input("Napisz wiadomość…")

if user_request:
    st.session_state.conversation.append({"role": "user", "content": user_request})
    with st.chat_message("user"):
        st.markdown(user_request)

    with st.chat_message("assistant"):
        activity = st.empty()
        activity_lines = []
        output_areas = {}
        output_text = {}
        final_state = None

        def label_for(namespace):
            path = "/".join(namespace)
            if "table-reservation-agent" in path:
                return "Subagent rezerwacji"
            return "Agent wyszukiwania restauracji"

        try:
            for namespace, mode, data in restaurant_finder_agent.stream(
                {"messages": st.session_state.conversation},
                stream_mode=["messages", "updates", "values"],
                subgraphs=True,
                version="v1",
            ):
                label = label_for(namespace)

                if mode == "messages":
                    message, metadata = data
                    token_text = text_from_content(getattr(message, "content", ""))
                    if token_text:
                        output_text[label] = output_text.get(label, "") + token_text
                        if label not in output_areas:
                            st.markdown(f"**{label}**")
                            output_areas[label] = st.empty()
                        output_areas[label].markdown(output_text[label])

                elif mode == "updates":
                    for node_name in data:
                        if node_name == "task":
                            activity_lines.append("Agent przekazuje zadanie subagentowi.")
                        elif node_name == "tools":
                            activity_lines.append(f"{label}: wykonuje narzędzie.")
                        elif node_name == "model":
                            activity_lines.append(f"{label}: analizuje wyniki.")
                    if activity_lines:
                        activity.markdown("\n\n".join(f"- {line}" for line in activity_lines[-8:]))

                elif mode == "values" and not namespace:
                    final_state = data

            if final_state and "messages" in final_state:
                st.session_state.conversation = final_state["messages"]
        except Exception as exc:
            st.error(f"Wystąpił błąd podczas działania agentów: {exc}")
