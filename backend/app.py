from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS Middleware Add Karo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Agar specific domain dena ho to ["https://ai-content-creator-iota.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContentRequest(BaseModel):
    topic: str
    content_type: str

@app.get("/")
def home():
    return {"message": "Backend is working perfectly!"}

@app.post("/generate")
def generate_content(request: ContentRequest):
    return {"content": f"Generated {request.content_type} about {request.topic}"}
