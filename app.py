from fastapi import FastAPI
from pydantic import BaseModel
from graph import chat_app

app = FastAPI()

class ChatRequest(BaseModel):
    user_message: str
    thread_id: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    state = {"messages": [req.user_message]}
    result = chat_app.invoke(state, config={"configurable": {"thread_id": req.thread_id}})
    return ChatResponse(response=result["messages"][-1])