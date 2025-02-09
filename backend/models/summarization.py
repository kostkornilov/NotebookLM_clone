# models/summarization.py
import openai
from config import OPENAI_API_KEY

def summarize_text(text: str, max_length: int = 150) -> str:
    """
    Summarize the provided text using OpenAI's GPT.
    """
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )

    summary = response["choices"][0]["message"]["content"]
    return summary
