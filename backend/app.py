from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ContentRequest(BaseModel):
    topic: str
    content_type: str

@app.get("/")
def home():
    return {"message": "Backend is working perfectly!"}

@app.post("/generate")
def generate_content(request: ContentRequest):
    if request.content_type == "blog":
        content = f"Generated blog about {request.topic}"
    elif request.content_type == "youtube_script":
        content = f"Generated YouTube script about {request.topic}"
    else:
        raise HTTPException(status_code=400, detail="Invalid content type")
    
    return {"content": content}
