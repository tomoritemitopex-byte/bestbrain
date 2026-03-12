
from fastapi import FastAPI
from orchestrator import BestBrain

app = FastAPI()
brain = BestBrain()

@app.get("/")
def home():
    return {"status": "BestBrain is running"}

@app.post("/ask")
def ask(prompt: str):
    return {"response": brain.process(prompt)}
