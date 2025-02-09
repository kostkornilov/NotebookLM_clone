from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load LoneStriker/gemma-7b-GGUF model from Hugging Face
MODEL_NAME = "LoneStriker/gemma-7b-GGUF"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Check if CUDA is available and set the device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if device == "cuda" else torch.float32).to(device)

def answer_question(query, context_texts):
    """Generate an answer using LoneStriker/gemma-7b-GGUF with retrieved text context."""
    context = "\n".join(context_texts)
    prompt = f"Context:\n{context}\n\nQ: {query}\nA:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)  # Use the appropriate device
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
