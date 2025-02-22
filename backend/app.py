from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API Key (Replace with your actual key)
OPENAI_API_KEY = "your-api-key"
openai.api_key = OPENAI_API_KEY

class ContentRequest(BaseModel):
    topic: str
    content_type: str  # "blog" or "youtube_script"

def generate_content(topic: str, content_type: str):
    prompt = f"Generate a {'YouTube script' if content_type == 'youtube_script' else 'SEO-friendly blog post'} on: {topic}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a content writer."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

@app.post("/generate")
async def generate(request: ContentRequest):
    try:
        content = generate_content(request.topic, request.content_type)
        return {"topic": request.topic, "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
