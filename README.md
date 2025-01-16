# ChatGPT Conversational Chatbot

Este é um projeto de chatbot conversacional utilizando a API do ChatGPT. Ele foi desenvolvido com Flask e integra uma API externa para enriquecer o contexto antes de fazer requisições à API do ChatGPT. O chatbot é projetado para responder de maneira agradável e clara, eliminando símbolos desnecessários das respostas.

## Funcionalidades

- Integração com uma API externa para busca de informações.
- Comunicação com o ChatGPT para gerar respostas conversacionais.
- Suporte a contexto dinâmico, permitindo que o chatbot entenda e responda perguntas com base em um histórico de conversas.

## Tecnologias Utilizadas

- Python
- Flask
- API do ChatGPT (OpenAI)
- Requests para chamadas HTTP

## Como Funciona

1. O endpoint `/teste` recebe uma requisição POST contendo:
   - `pergunta`: A pergunta do usuário.
   - `contexto`: Um histórico de perguntas e respostas anteriores para manter a conversação.
   
2. O sistema faz uma requisição à API externa para buscar informações adicionais.

3. Com os dados obtidos, o sistema constrói um prompt detalhado e envia uma requisição para a API do ChatGPT.

4. O ChatGPT responde com uma mensagem formatada, que é retornada ao usuário.
