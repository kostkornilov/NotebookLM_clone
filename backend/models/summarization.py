# models/summarization.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "LoneStriker/gemma-7b-GGUF"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if device == "cuda" else torch.float32).to(device)

def summarize_text(text: str, max_new_tokens: int = 150) -> str:
    """
    Summarize the provided text using LoneStriker/gemma-7b-GGUF.
    """
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary
