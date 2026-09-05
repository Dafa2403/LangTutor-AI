import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from src import GROQ_API_KEY, get_llm_tutor

st.title("🎓 LangTutor AI")

AI_AVATAR = "assets/LangTutor.jpg"

if not GROQ_API_KEY or not GROQ_API_KEY.strip():
    st.error("API Key Groq tidak ditemukan di config. Periksa file .env kamu!")
    st.stop()

if "name" not in st.session_state:
    st.session_state['name'] = ""
if "language" not in st.session_state:
    st.session_state["language"] = ""

if not st.session_state['name']:
    st.subheader("Step 1 of 2: What is your name?")
    
    col1, col2 = st.columns([80, 20])
    with col1:
        input_name = st.text_input(
            "Name",
            label_visibility="collapsed",
            placeholder="Type your name here...",
        )
    with col2:
        if st.button("Next", key="btn_name"):
            if input_name.strip():
                st.session_state['name'] = input_name.strip()
                st.rerun() 
            else:
                st.warning("Name cannot be empty!")
                
    st.stop()

if st.session_state['name'] and not st.session_state["language"]:
    st.subheader(f"Hello {st.session_state['name']}! Choose your target language:")
    
    selected_lang = st.selectbox(
        "Language",
        ["English", "Japanese", "German", "Indonesian", "Mandarin", "Russian"],
        label_visibility="collapsed"
    )
    
    if st.button("Start Chat", key="btn_lang"):
        st.session_state["language"] = selected_lang
        st.rerun()
        
    st.stop()

name = st.session_state['name']
language = st.session_state["language"]

msgs = StreamlitChatMessageHistory(key="langtutor_messages")
tutor_chain = get_llm_tutor(msgs)

if len(msgs.messages) == 0:
    welcome_msg = (
        f"Welcome {name}! I am Lang, your AI language tutor for {language}. "
        f"What would you like to learn today? Please type your question or topic."
    )
    msgs.add_ai_message(welcome_msg)

for msg in msgs.messages:
    if msg.type == "human":
        with st.chat_message("human"):
            st.write(msg.content)
    else:
        with st.chat_message("ai", avatar=AI_AVATAR):
            st.write(msg.content)

if user_input := st.chat_input("Type your message here..."):
    st.chat_message("human").write(user_input)

    config = {"configurable": {"session_id": "langtutor_session"}}
    response = tutor_chain.invoke(
        {
            "user_name": name, 
            "target_language": language, 
            "question": user_input
        },
        config=config
    )

    st.chat_message("ai", avatar=AI_AVATAR).write(response.content)

    