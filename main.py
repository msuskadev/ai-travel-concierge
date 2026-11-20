import time

import streamlit as st
from dotenv import load_dotenv
from langfuse.langchain import CallbackHandler

st.set_page_config(page_title="Trip Planner", page_icon="✈️", layout="wide")
st.markdown(
    """
    <style>
      .block-container { max-width: 100%; padding: 1.5rem 2.5rem 2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

load_dotenv()
# langfuse_handler = CallbackHandler()

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


def message_field(message, field, default=None):
    if isinstance(message, dict):
        return message.get(field, default)
    return getattr(message, field, default)


def render_usage_panel(messages):
    assistant_messages = [m for m in messages if message_role(m) == "assistant"]
    st.subheader("Szczegóły odpowiedzi")
    if not assistant_messages:
        st.caption("Metadane i koszty pojawią się po pierwszej odpowiedzi.")
        return

    latest = assistant_messages[-1]
    metadata = message_field(latest, "response_metadata", {}) or {}
    usage = message_field(latest, "usage_metadata", {}) or {}
    cost = metadata.get("cost")
    total_tokens = usage.get("total_tokens")
    cost_label = f"${cost:.6f}" if isinstance(cost, (int, float)) else "—"
    token_label = f"{total_tokens:,}" if isinstance(total_tokens, int) else "—"
    cost_col, token_col = st.columns(2)
    cost_col.metric("Koszt", cost_label)
    token_col.metric("Tokeny", token_label)
    ttft = st.session_state.get("latest_ttft_seconds")
    st.metric("TTFT", f"{ttft:.2f} s" if ttft is not None else "—")
    st.caption(
        f"Wejściowe: {usage.get('input_tokens', '—')} · "
        f"Wyjściowe: {usage.get('output_tokens', '—')}"
    )
    st.caption(f"Model: {metadata.get('model_name') or '—'}")
    with st.expander("Metadane odpowiedzi", expanded=False):
        st.json(metadata or {"info": "Brak metadanych odpowiedzi"})
        if usage:
            st.markdown("**Zużycie tokenów**")
            st.json(usage)

st.session_state.setdefault("conversation", [])
st.session_state.setdefault("latest_ttft_seconds", None)

main_col, details_col = st.columns([7, 3], gap="large")
with main_col:
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
        content = text_from_content(message_field(message, "content", ""))
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
            request_started_at = time.perf_counter()
            st.session_state.latest_ttft_seconds = None

            try:
                for namespace, mode, data in trip_planner_agent.stream(
                    {"messages": st.session_state.conversation},
                    stream_mode=["messages", "values"],
                    subgraphs=True,
                    version="v1",
                    # config={"callbacks": [langfuse_handler]},
                ):
                    if mode == "messages" and not namespace:
                        message, _metadata = data
                        token_text = text_from_content(getattr(message, "content", ""))
                        if token_text:
                            if st.session_state.latest_ttft_seconds is None:
                                st.session_state.latest_ttft_seconds = (
                                    time.perf_counter() - request_started_at
                                )
                            streamed_response += token_text
                            response_area.markdown(streamed_response)
                    elif mode == "values" and not namespace:
                        final_state = data

                if final_state and "messages" in final_state:
                    st.session_state.conversation = final_state["messages"]
                    response_area.markdown(
                        text_from_content(message_field(final_state["messages"][-1], "content", ""))
                    )
            except Exception as exc:
                st.error(f"Wystąpił błąd podczas działania agentów: {exc}")

with details_col:
    render_usage_panel(st.session_state.conversation)
