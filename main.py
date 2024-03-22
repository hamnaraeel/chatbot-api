from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Prompt(BaseModel):
    text: str

@app.post("/chat/")
async def chat_with_openai(prompt: Prompt):
    openai.api_key = "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"
    try:
        # Using the incoming prompt text in the messages list
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the chat model you're using
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.text}  # Use the incoming prompt text here
            ],
            temperature=0.7,
            max_tokens=150
        )
        return {"response": response.choices[0].message["content"].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
