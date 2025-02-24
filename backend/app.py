from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change to specific domain if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return {"message": "Backend is working perfectly!"}

@app.post("/generate")
async def generate_content(data: dict):
    topic = data.get("topic", "Default Topic")
    content_type = data.get("content_type", "blog")
    return {"content": f"Generated {content_type} about {topic}"}
