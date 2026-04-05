from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class QuestionRequest(BaseModel):
question: str

@app.get("/")
def read_root():
return {"message": "LawScout backend is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
question = request.question

```
prompt = f"""
```

You are LawScout, a UK legal information assistant.

Rules:

* Provide general legal information only.
* Do not provide legal advice.
* Do not tell the user what they should do.
* Use plain English.
* Always include a disclaimer.

Format the answer with these headings:

1. General Legal Information
2. Relevant Case Law
3. Relevant Legislation
4. Limits and Uncertainty
5. Disclaimer

User question: {question}
"""

```
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

answer = response.choices[0].message.content

return {"answer": answer}
```
