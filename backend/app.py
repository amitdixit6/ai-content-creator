from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS Middleware (Fix Cross-Origin Issues)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🟢 Allow All Origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is working perfectly!"}

# ✅ Fix: Add the `/generate` route
@app.post("/generate")
def generate_content(request_data: dict):
    topic = request_data.get("topic", "AI")
    content_type = request_data.get("content_type", "blog")

    # Dummy content generation (Replace with AI logic if needed)
    generated_text = f"Generated {content_type} about {topic}"

    return {"content": generated_text}

