class Chatbot():
    def __init__(self, nome):
        self.nome = nome
        self.conhecidos = ['Will','João']
        self.historico = []

    def escuta(self):
        frase = input('>: ')
        frase = frase.lower()
        frase = frase.replace('é','eh')
        return frase
        pass

    def pensa(self, frase):
        if frase == ('oi'):
            return 'Olá, qual seu nome?'
        if self.historico[-1] == 'Olá, qual seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        return 'Não entendi!'

    def pegaNome(self, nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:]
            
        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            frase = 'Muito prazer '

        return frase+nome

    def fala(self, frase):
        print(frase)
        self.historico.append(frase)