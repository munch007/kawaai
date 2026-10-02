from openai import OpenAI
client = OpenAI()

question=input("You:")
response=client.responses.create(
    model="gpt-5",
    input=question
)

print("AI:", response.output_text)
