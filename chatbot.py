def resposta():
    resp = input('>: ')
    resp = resp.lower()
    resp = resp.replace('é','eh')
    return resp

print('Olá, qual o seu nome?')

if 'o meu nome eh ' in nome:
    nome = nome[14:]

resp = resp.title()

conhecidos = ['Raimundo','Will','Joao']

frase = 'Muito prazer '
if conhecidos in conhecidos:
    frase = 'Eaew '
else:
    frase = 'Muito prazer '

print(frase+nome)

while True:
    resp = input('>: ')
    if resposta == 'tchau':
        break
    else:
        print('Digite outra coisa')

print('Tchau tchau!')