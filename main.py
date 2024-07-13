from fastapi import FastAPI, HTTPException, Query
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
    openai.api_key = "sk-proj-AHYEGGxzVvSMs0aWsRuQT3BlbkFJ0g4vsh52Y86MtyAWUMxu"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.text}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return {"response": response.choices[0].message["content"].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/chat/")
async def chat_with_openai_get(query: str = Query(..., description="Who are you?")):
    openai.api_key = "sk-proj-AHYEGGxzVvSMs0aWsRuQT3BlbkFJ0g4vsh52Y86MtyAWUMxu"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return {"response": response.choices[0].message["content"].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
