#Define as variáveis
pontuacao  = 0
sua_resposta = ""
questao01  = 'Qual é o nome do Ex-Baterista da banda Canadense "Rush"? \n(A) John Bonham \n(B) Neil Peart \n(C) Keith Moon \n(D) Ginger Baker'
resposta01 = 'B'
questao02  = 'Qual é o álbum do Pink Floyd que homenageia o ex-integrante Syd Barrett? \n(A) The Wall \n(B) The Dark Side of the Moon \n(C) Wish You Were Here \n(D) Animals'
resposta02 = 'C'
questao03  = 'Qual dessas bandas não é um "Power Trio"? \n(A) Green Day \n(B) Nirvana \n(C) Cream \n(D) Led Zeppellin'
resposta03 = 'D'
questao04  = 'Quem foi que popularizou o sinal de dedo "Chifre do Diabo"? \n(A) Ronnie James Dio \n(B) Ozzy Osborne \n(C) Alice Cooper \n(D) Dave Mustaine'
resposta04 = 'A'
questao05  = 'Dave Grohl não participou de qual dessas bandas? \n(A) Foo Fighters \n(B) Nirvana \n(C) Them Crooked Vultures \n(D) Muse'
resposta05 = 'D'

#Listas com as mensagens de acordo com a pontuação
frases_pontuacao = ["Você tocou no botão errado da guitarra da vida. Tente novamente!", "Há potencial, mas você ainda não desbloqueou o modo rockstar.", "Bem na média. Dá para tocar uma baladinha, mas evite os solos.", "Você está no caminho certo! Quem sabe você não forma sua própria banda?", "Uau! Você é praticamente uma lenda do rock! Continue assim!", "Parabéns! Você atingiu o nível máximo de excelência musical. A platéia está em êxtase!"]

#Dicionário com perguntas e respostas
perguntas_respostas = {questao01: resposta01, questao02: resposta02, questao03: resposta03, questao04: resposta04, questao05: resposta05}

#Printa as Boas vindas do jogo
print('**************************************')
print('Bem vindo ao quiz de música em Python!')
print('**************************************')

#Mostra as perguntas e pergunta a resposta do jogador
for pergunta, resposta in perguntas_respostas.items():
    print(pergunta)
    sua_resposta = input('Qual sua resposta?: ')
# Verifica se a resposta está correta
    if sua_resposta.upper() == resposta:
        print('Acertou!\n')
        pontuacao += 1
    else:
        print('Errou!\n')

# Mostra a pontuação final
print('**************************************')
print('Pontuação Final:', pontuacao)
print(frases_pontuacao[pontuacao])
print('**************************************')




