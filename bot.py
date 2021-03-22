#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skpy import Skype
import sys

# Variaveis -------------------------

# Dados de login do usuario
user = 'EMAIL'
passwd = 'SENHA'

# Instancia um objeto SkypeActions
bot = Skype(user, passwd)

# Id's dos grupos
groups = {
	1: '19:dd8f2c92cad34c2f922997e06064788f@thread.skype',
	2: '19:14fbb4909a6140c1816699be53821e29@thread.skype'
}

# Palavras chave para procurar
keywords = {
	1: ['tradução', 'traduções', 'TR'],
	2: ['disponível', 'disponibilidade'],
	3: ['filme', 'série', 'episódio', 'episódios', 'projeto', 'task'],
	4: ['entrega', 'entregas', 'até']
}

# Controle de instancia
firstInstance = 1

# Funções -------------------------

# Verifica se a mensagem passada segue os parametros de match
def verifyKeywordsMatch(message):
	# Importa as variaveis
	global keywords

	# Controle de resultados
	groupRes = {
		1: False,
		2: False,
		3: False,
		4: False
	}

	# Loop em keywords
	for wordsGroup in keywords:
		# Pega o grupo de palavras atual
		words = keywords[wordsGroup]

		# Loop em wordsGroup
		for word in range(0, len(words)):
			# Verifica se a palavra existe na mensagem
			if message.find(words[word]) != -1:
				# Define a combinação do grupo 1 como sucedida
				groupRes[wordsGroup] = True
				
				# Encerra o lopp em wordsGroup
				break
			elif message.find(words[word].upper()) != -1:
				# Define a combinação do grupo 1 como sucedida
				groupRes[wordsGroup] = True
				
				# Encerra o lopp em wordsGroup
				break
			elif message.find(words[word].capitalize()) != -1:
				# Define a combinação do grupo 1 como sucedida
				groupRes[wordsGroup] = True
				
				# Encerra o lopp em wordsGroup
				break

	# Verifica os resultados das verificações
	if groupRes[1] == True and groupRes[2] == True and groupRes[3] == True and groupRes[4] == True:
		# Retorna True
		return True
	else: 
		print("Res 1 => ")
		print(groupRes[1])
		print('')
		print("Res 2 => ")
		print(groupRes[2])
		print('')
		print("Res 3 => ")
		print(groupRes[3])
		print('')
		print("Res 4 => ")
		print(groupRes[4])
		print('')
		# Retorna False
		return False


# Eecuta os métodos necessários para o funcionamento do script
def run(bot):
	# Importa as variaveis
	global groups
	global firstInstance

	# Entra no chat do grupo 1
	chat = bot.chats[groups[1]]

	# Recupera as mensagens do grupo
	messages = chat.getMsgs()

	# Verifica se é a primeira instancia do script
	if firstInstance == 1 or firstInstance == 2:
		# Previne o bloqueio das proximas instancias
		firstInstance += 1

		# Encerra a função
		return

	# Verifica se existem novas mensagens
	if len(messages) <= 0:
		# Encerra a função para evitar erros de index
		return

	# Pega a ultima mensagem
	lastMessage = messages[0]

	try:
		# Guarda o conteudo formatado da mensagem
		message = lastMessage.plain
	except Exception as e:
		print("Pulando...")
		return


	# Verifica se a mensagem cumpre os requisitos de procura
	keywordsMatch = verifyKeywordsMatch(message)

	# Verifica o resultado da verificação
	if keywordsMatch == True:
		# Entra no chat do grupo 2
		chat = bot.chats[groups[2]]

		# Envia a mensagem de interesse para o grupo 2
		chat.sendMsg("Eu!")

		# Printa para o usuario que uma mensagem foi encontrada
		print('Combinação encontrada. Uma mensagem foi enviado para o Grupo 2.')
		print('Saindo do programa...')
		print('')

		# Encerra o programa
		sys.exit()


# Printa a mensagem de boas vindas para o usuario
print('Iniciado o SkpyBot - 1.0.0')
print('Analisando mensagens...')
print('')

# Loop principal
while True:
	run(bot)
