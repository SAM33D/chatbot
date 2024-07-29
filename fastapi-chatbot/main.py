from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = "sk-proj-AFgjhIQ1CcGlrgM0e9mfT3BlbkFJ7SfFk0RqO0axs0DHb3ef"

@app.get("/")
def read_root():
    return {"Welcome to the FastAPI Chatbot!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=user_message,
        max_tokens=150
    )
    
    chatbot_response = response.choices[0].text.strip()
    
    return {"response": chatbot_response}
