from fastapi import FastAPI
from pydantic import BaseModel
from logic import generate_response

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/query")
def query_agent(body: Query):
    reply = generate_response(body.message)
    return {
        "reply": reply
    }
