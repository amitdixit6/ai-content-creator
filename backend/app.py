from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# ✅ CORS Enable
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 Vercel aur frontend ke liye allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ OpenAI API Key (set environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Request Body Model
class ContentRequest(BaseModel):
    topic: str
    content_type: str

# ✅ Home Route
@app.get("/")
def home():
    return {"message": "Backend is working perfectly!"}

# ✅ AI Content Generator Route
@app.post("/generate")
def generate_content(request: ContentRequest):
    try:
        prompt = f"Write a {request.content_type} about {request.topic}"
        
        # OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        content = response["choices"][0]["message"]["content"]

        return {"content": content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
