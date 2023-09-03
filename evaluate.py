import openai
import json
from decouple import config



def evaluate(trained_response_path,submission_path,input_argument):
    openai.api_key = config('OPEN_AI_API_KEY')

    with open(f"{submission_path}/f{input_argument}.c",'r') as code_file:
        code = code_file.read()

    with open(f"{trained_response_path}/response{input_argument}.json",'r') as json_file:
        messages = json.load(json_file)
    print(messages)
    print(code)
    messages.append({"role":"user","content":code})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})

    with open(f"{submission_path}/DETAILS0{input_argument}.txt",'w') as file:
        file.write(reply)
    # jsonString = json.dumps(messages)
    # with open(f"{submission_path}/response{input_argument}.json",'w') as outfile:
    #     outfile.write(jsonString)
    print(reply)


