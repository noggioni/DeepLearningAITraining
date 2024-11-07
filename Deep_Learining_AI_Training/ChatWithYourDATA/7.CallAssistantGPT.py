import os
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Define a function to interact with the assistant
def call_assistant(prompt):
    # Start a new thread
    thread = client.beta.thread.create_and_run(
        model="asst_5JdS8ufL8okfXrS5ud8OFVSC"  # Replace with your correct assistant model ID
    )
    
    # Run the assistant within this thread
    response = thread.run(
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

# Example usage
account = input("Enter the customer name --> ")
language = input("Enter the output language --> ")
prompt = f"[CUSTOMER={account}, LANG={language}]"
response = call_assistant(prompt)
print("Assistant Response:", response)
