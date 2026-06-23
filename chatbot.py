from funções import *

print('Olá, qual o seu nome?')
nome = pegaOnome(resposta())
resp = respondeNome(nome)
print(resp)

while True:
    resp = resposta()
    if resp == 'tchau':
        break
    else:
        print('Digite outra coisa')

print('Tchau tchau!')