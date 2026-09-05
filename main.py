from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_core.chat_history import InMemoryChatMessageHistory
from src import get_llm_tutor

app = Flask(__name__)
CORS(app)

sessions_db = {}

def get_session_history(session_id: str):
    if session_id not in sessions_db:
        sessions_db[session_id] = InMemoryChatMessageHistory()
    return sessions_db[session_id]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    session_id = data.get("session_id") #Unique session identifier :str
    user_name = data.get("name", "")
    target_language = data.get("language", "")
    user_message = data.get("message", "")

    if not user_message.strip():
        return jsonify({"Error": "User message cannot be empty."}), 400
    if not user_name.strip():
        return jsonify({"Error": "User name cannot be empty."}), 400
    if not target_language.strip():
        return jsonify({"Error": "User target language cannot be empty."}), 400

    memory_history = get_session_history(session_id)
    tutor = get_llm_tutor(memory_history)

    config = {"configurable": {"session_id": session_id}}

    response = tutor.invoke(
        {
            "user_name": user_name,
            "target_language": target_language,
            "question": user_message,
        },
        config=config
    )

    return jsonify({
        "status": "success",
        "session_id": session_id,
        "response": response.content
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)