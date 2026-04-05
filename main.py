from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
return {"message": "LawScout backend is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
if not api_key:
return {"answer": "Server error: OPENAI_API_KEY is missing."}

```
prompt = f"""
```

You are LawScout, a UK legal information assistant.

Rules:

* Provide general legal information only
* Do not provide legal advice
* Do not tell the user what they should do
* Use plain English
* Keep the answer structured under these headings:

  1. General Legal Information
  2. Relevant Case Law
  3. Relevant Legislation
  4. Limits and Uncertainty
  5. Disclaimer

User question:
{request.question}
"""

```
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

return {"answer": response.output_text}
```

)

return {"answer": response.output_text}
```
