#Descrição da Tarefa:

Você deve desenvolver um sistema que atenda aos seguintes requisitos:

<Frontend>
Crie uma página HTML que contenha:
Uma caixa de texto onde o usuário possa inserir um valor (por exemplo, um número).
Um botão que, quando pressionado, envie o conteúdo da caixa de texto para o servidor.
Após receber uma resposta do servidor, exiba na página o número de vezes que o valor enviado foi recebido pelo servidor desde que o mesmo foi iniciado.

<Backend>
O servidor deve ser capaz de:
Receber o conteúdo enviado pelo frontend (via requisição HTTP, como POST ou GET).
Manter uma contagem de quantas vezes cada valor foi recebido. Para isso, é recomendado usar uma estrutura como uma tabela (por exemplo, em um arquivo ou em uma estrutura de dados na memória).
Retornar o número atualizado de vezes que o valor foi recebido.
