from flask import Flask, jsonify, request
import requests
from requests.auth import HTTPBasicAuth
from credentials import API_KEY, USERNAME, PASSWORD, URL
import json

app = Flask(__name__)

@app.route('/teste', methods=['POST'])
def teste():
    dados = request.get_json()
    pergunta = dados.get('pergunta')
    contexto = dados.get('contexto')

    # Faz requisição na api da cliente
    url_cliente = URL

    username = USERNAME
    password = PASSWORD

    client_id = '3101'

    headers_cliente = {
        'clientID': client_id,
        'Content-Type': 'application/json'
    }

    response = requests.get(url_cliente, auth=HTTPBasicAuth(username, password), headers=headers_cliente)

    response.encoding = 'utf-8'
    data = response.json()
    print(data)

    #Faz requisição para o chatGPT
    url_gpt = "https://api.openai.com/v1/chat/completions"
    
    headers_gpt = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    messages = [
        {
                "role": "system",
                "content": """
                    Você é um assistente agradável. 
                    Traga a responsta em um texto corrido.
                    Para informações que não constam nos dados responda: Essa informação não existe na plataforma.
                    Tire o seguinte simbolo de todas as respostas: \. 
                """
        }
    ]

    for data in contexto:
        messages.append({"role": "user", "content": data["pergunta"]})
        messages.append({"role": "assistant", "content": data["resposta"]})
    
    messages.append({"role": "user", "content": f"{pergunta}. Aqui estão os dados: {data}"})
    
    body_message = {
        "model": "gpt-4o",
        "messages": messages
    }
    
    body_message = json.dumps(body_message)

    response_gpt = requests.post(url_gpt, headers=headers_gpt, data=body_message)

    # Resposta do chatGPT
    resposta_chatbot = response_gpt.json()["choices"][0]["message"]["content"]

    if response.status_code == 200:
        return json.dumps(resposta_chatbot)
    else:
        return jsonify({"erro": "Falha na autenticação ou erro na API externa"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5000)