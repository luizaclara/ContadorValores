# Sistema de Contagem de Requisições

Este é um sistema simples que possui uma interface frontend em HTML e um backend para contar quantas vezes um valor enviado foi recebido pelo servidor.

## Descrição

O sistema possui duas partes principais:

### Frontend
- Uma página HTML com uma caixa de texto onde o usuário pode inserir um valor (por exemplo, um número).
- Um botão que, ao ser pressionado, envia o valor para o servidor.
- Após a resposta do servidor, a página exibe o número de vezes que o valor enviado foi recebido desde o início do servidor.

### Backend
- O servidor recebe o conteúdo enviado pelo frontend via requisição HTTP (GET ou POST).
- Mantém uma contagem de quantas vezes cada valor foi recebido. Isso é feito usando uma estrutura de dados (como uma tabela ou dicionário) armazenada na memória ou em um arquivo.
- O servidor retorna a quantidade 

## Tecnologias Utilizadas

- **Frontend**: HTML, JavaScript
- **Backend**: Python (Flask)
