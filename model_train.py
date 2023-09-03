import openai
import json
from decouple import config



def train_gpt_model(prompt_path,response_path,input_argument):
    openai.api_key = config('OPEN_AI_API_KEY')
    with open(f"{prompt_path}/Question{input_argument}.txt",'r') as prompt_file:
        prompt = prompt_file.read()
    messages = []
    print(prompt)
    messages.append({"role":"user","content":f"{prompt}"})

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    response = messages
    jsonString = json.dumps(response)
    with open(f"{response_path}/response{input_argument}.json",'w') as outfile:
        outfile.write(jsonString)
    
    print(reply)

