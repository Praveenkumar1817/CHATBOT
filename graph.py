from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class ChatState(TypedDict):
    messages: list[str]

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def bot_node(state: ChatState):
    # In graph.py, inside bot_node:
    user_message = state["messages"][-1]

    # Optional: Add system-like instruction if document is detected
    # (But since we're embedding context in the message, this may not be needed)

    try:
        response = model.generate_content(
            user_message,
            generation_config={"temperature": 0.8}  # more deterministic for QA
        )
        reply = (response.text or "⚠ No reply generated.").strip()
    except Exception as e:
        reply = f"⚠ Error: {e}"

memory = MemorySaver()
graph = StateGraph(ChatState)
graph.add_node("bot", bot_node)
graph.set_entry_point("bot")
graph.add_edge("bot", END)

chat_app = graph.compile(checkpointer=memory)