import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = input("Frage:\n")

response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
    {'role': 'user',
     'content': f'{prompt}'}
    ])

print("Antwort:")
print(response['choices'][0]['message']['content'])

