import os

from openai import OpenAI

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )


from openai import OpenAI
client = OpenAI()

run = client.beta.threads.create_and_run(
  assistant_id="asst_5JdS8ufL8okfXrS5ud8OFVSC",
  thread={
    "messages": [
      {"role": "user", "content": "CUSTOMER=Avianca"}
    ]
  }
)

print(run)
# Define a function to call the assistant
def call_assistant(prompt):
    response = client.beta.threads.create_and_run(
        assistant_id="asst_5JdS8ufL8okfXrS5ud8OFVSC",
        thread={
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    return response[-1]

# Example usage
account = input("Enter the customer name --> ")
language = input("Eter the output Languange --> ")
prompt = f"[CUSTOMER={account}, LANG={language}]"
ask = call_assistant(prompt)
print("Assistant Response:")
print(ask)
