import os

### import utils
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

###Exercise Instructions
prompt = "what is 1 + 1"
context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders
             """}
]
context.append({'role':'user', 'content':f"{prompt}"})
response = get_completion_from_messages(context) 
print(response)

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
style = """American English \
in a calm and respectful tone
"""
prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""

print(prompt)

context.append({'role':'user', 'content':f"{prompt}"})
response = get_completion_from_messages(context) 
print(response)
