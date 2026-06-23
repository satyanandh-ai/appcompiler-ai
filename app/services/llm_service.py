from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_app_plan(prompt: str):
    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1
    )

    return result[0]["generated_text"]