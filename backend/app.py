from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS Middleware Fix (Backend se frontend request allow)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Agar sirf Vercel allow karna ho toh: ["https://ai-content-creator-iota.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],  # POST, GET sab allow hoga
    allow_headers=["*"],  
)

@app.get("/")
def home():
    return {"message": "Backend is working perfectly!"}

@app.post("/generate")
def generate_content(data: dict):
    topic = data.get("topic", "No topic provided")
    content_type = data.get("content_type", "blog")
    
    # Dummy AI response (replace with OpenAI API call if needed)
    generated_content = f"Generated {content_type} about {topic}"
    
    return {"content": generated_content}
