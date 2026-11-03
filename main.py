import streamlit as st
from dotenv import load_dotenv
from langfuse.langchain import CallbackHandler

st.set_page_config(page_title="Trip Planner", page_icon="✈️")

load_dotenv()
langfuse_handler = CallbackHandler()

from agents.trip_planner import trip_planner_agent


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

st.session_state.setdefault("conversation", [])

logo_col, title_col, reset_col = st.columns(
    [2, 5, 1], vertical_alignment="center"
)
with logo_col:
    st.image("assets/logo.jpg", width=150)
with title_col:
    st.markdown(
        "<h1 style='text-align: center;'>AI Travel Concierge</h1>",
        unsafe_allow_html=True,
    )
with reset_col:
    st.write("")
    reset_conversation = st.button("Nowe zapytanie", icon="➕", use_container_width=True)

if reset_conversation:
    st.session_state.conversation = []
    st.rerun()

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
        response_area = st.empty()
        streamed_response = ""
        final_state = None

        try:
            for namespace, mode, data in trip_planner_agent.stream(
                {"messages": st.session_state.conversation},
                stream_mode=["messages", "values"],
                subgraphs=True,
                version="v1",
                config={"callbacks": [langfuse_handler]},
            ):
                if mode == "messages":
                    if not namespace:
                        message, _metadata = data
                        token_text = text_from_content(getattr(message, "content", ""))
                        if token_text:
                            streamed_response += token_text
                            response_area.markdown(streamed_response)

                elif mode == "values" and not namespace:
                    final_state = data

            if final_state and "messages" in final_state:
                st.session_state.conversation = final_state["messages"]
        except Exception as exc:
            st.error(f"Wystąpił błąd podczas działania agentów: {exc}")
