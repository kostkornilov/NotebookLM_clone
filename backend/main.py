from fastapi import FastAPI
from routes import documents, chat

app = FastAPI(title="NotebookLM Clone")

app.include_router(documents.router, prefix="/documents", tags=["Documents"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def read_root():
    return {"message": "Welcome to NotebookLM Clone!"}
