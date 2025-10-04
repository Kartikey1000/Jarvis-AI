from openai import OpenAI

# Initialize the client
client = OpenAI(
    api_key="AIzaSyBpQoift-LKZjMzS1Pp2LazLJbNL5IXdxE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Chat completion using a valid model from your list
completion = client.chat.completions.create(
    model="gemini-flash-latest",   # <-- Pick a model from the printed list
    messages=[
        {"role": "system", "content": "You are Jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
