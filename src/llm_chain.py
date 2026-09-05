from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory
from src.config import GROQ_API_KEY, DEFAULT_MODEL
from src.prompts import prompt

def get_llm_tutor(memory_history):
    client = ChatGroq(
        model=DEFAULT_MODEL, 
        api_key=GROQ_API_KEY,
        temperature=0.7,
    )

    chain = prompt | client

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: memory_history,
        input_messages_key="question",
        history_messages_key="history",
    )

    return chain_with_history
