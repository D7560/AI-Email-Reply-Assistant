from fastapi import FastAPI
from pydantic import BaseModel
from model import load_model, generate_reply
from utils import preprocess_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once
model, tokenizer = load_model()

class EmailRequest(BaseModel):
    email: str
    tone: str
    max_tokens: int

@app.post("/generate_reply")
def generate_email_reply(request: EmailRequest):
    cleaned = preprocess_email(request.email)
    prompt = f"Reply in a {request.tone.lower()} tone to this email:\n\n{cleaned}\n\nReply:"
    reply = generate_reply(model, tokenizer, prompt, max_tokens=request.max_tokens)
    return {"reply": reply}
