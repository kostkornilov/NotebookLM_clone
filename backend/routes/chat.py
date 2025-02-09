from fastapi import APIRouter
from pydantic import BaseModel
from models.embeddings import vector_store
from models.qa import answer_question

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/ask/")
async def ask_question(request: QueryRequest):
    relevant_texts = vector_store.search(request.query)
    response = answer_question(request.query, relevant_texts)
    return {"answer": response}
