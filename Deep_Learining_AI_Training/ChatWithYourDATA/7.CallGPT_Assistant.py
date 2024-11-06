import os

from openai import OpenAI

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message.content


# Define a function to call the assistant
def call_assistant(prompt):
    response = client.chat.completions.create(
        model="asst_5JdS8ufL8okfXrS5ud8OFVSC",  # Assistant Name
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
prompt = "[CUSTOMER=TEcnoquimicas, LANG=Spanish]"
response = call_assistant(prompt)
print("Assistant Response:")
print(response)
