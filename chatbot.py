import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}Veja bem, {nome}, lixo eletrônico, Resíduos de Equipamentos Elétricos e eletrônicos (REEE) ou e-lixo são termos utilizados para se referir a todos os equipamentos elétricos e eletrônicos. Saiba mais em: https://www.ecycle.com.br/1823-reciclagem-de-eletronicos.html{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}É possível colaborar com a causa descartando o lixo eletrônico da maneira certa, no ponto de coleta mais próximo. O nosso site oferece um mapa que mostra os principais pontos de coleta próximos a você{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}Para utilizar o mapa integrado ao site, acesse esse link {os.linesep}')
    
    else:
        print('Digite apenas 1, 2 ou 3, por favor')

def start():
    #apresentar o chatbot
    print(f'Olá, bem vindo ao site do TechSave, em que posso ajudar? {os.linesep} {os.linesep}')

    #pedir nome
    nome = input('Digite seu nome: ')

    #oferecer menu de opções
    resposta = input(f'[1]: O que é lixo eletrônico?{os.linesep}[2]: Como eu posso colaborar com o projeto?{os.linesep}[3]: Quero descartar meu lixo eletrônico corretamente, como posso fazer isso?{os.linesep}')

     #processara resposta enviada
    processar_resposta(resposta,nome)


    while True: 
        #oferecer menu de opções
        resposta = input(f'O que mais você quer saber? {os.linesep}[1]: O que é lixo eletrônico?{os.linesep}[2]: Como eu posso colaborar com o projeto?{os.linesep}[3]: Quero descartar meu lixo eletrônico corretamente, como posso fazer isso?{os.linesep}')

        #processara resposta enviada
        processar_resposta(resposta,nome)


if __name__ == '__main__':
    start()