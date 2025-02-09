import openai
from config import OPENAI_API_KEY

def answer_question(query, context_texts):
    """Generate an answer using GPT with retrieved text context."""
    context = "\n".join(context_texts)
    prompt = f"Context:\n{context}\n\nQ: {query}\nA:"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )

    return response["choices"][0]["message"]["content"]
