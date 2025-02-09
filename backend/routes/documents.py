import os
from fastapi import APIRouter, UploadFile, File
from models.text_extraction import extract_text
from config import DATA_STORAGE_PATH
from models.embeddings import vector_store

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    os.makedirs(DATA_STORAGE_PATH, exist_ok=True)  # Ensure the directory exists
    file_path = os.path.join(DATA_STORAGE_PATH, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)
    vector_store.add_texts(text.split("\n"))  # Split text into chunks
    return {"filename": file.filename, "message": "Document processed successfully!"}

