from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "LawScout backend is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "answer": f"Test response from LawScout backend. Your question was: {request.question}"
    }
