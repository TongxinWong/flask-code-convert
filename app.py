import openai
from flask import Flask, request
app = Flask(__name__)

openai.api_key = "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" # os.getenv("OPENAI_API_KEY")
openai.model = "gpt-3.5-turbo"
history = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {knowledge_cutoff} Current date: {current_date}"}]

@app.route('/api/code_convert', methods=['POST'])
def code_convert():
    received_data = request.get_json()
    input_lang = received_data['input_lang']
    output_lang = received_data['output_lang']
    input_code = received_data['input_code']
    # use open ai to convert code
    history = [{"role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {knowledge_cutoff} Current date: {current_date}. Now you are mainly focused on code type conversion, you do not need to give any additional explanation, you just need to give the converted code."}]

    prompt = f"Input language: {input_lang}\nInput code: {input_code}\nOutput language: {output_lang}\nOutput code:"
    history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= history
    )
    ret = response["choices"][0]["message"]['content']
    return ret

# @app.route('/api/code_convert', methods=['GET'])
# def code_convert():
#     # input_lang = request.args.get('input_lang')
#     # output_lang = request.args.get('output_lang')
#     # input_code = request.args.get('input_code')
#     input_lang = "Python"
#     output_lang = "C++"
#     input_code = "print('Hello World')"
#     # use open ai to convert code
#     history = [{"role": "system",
#                 "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {knowledge_cutoff} Current date: {current_date}. Now you are mainly focused on code type conversion, you do not need to give any additional explanation, you just need to give the converted code."}]

#     prompt = f"Input language: {input_lang}\nInput code: {input_code}\nOutput language: {output_lang}\nOutput code:"
#     history.append({"role": "user", "content": prompt})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages= history
#     )
#     ret = response["choices"][0]["message"]['content']
#     return ret

# if __name__ == '__main__':
#     app.run()
