#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skpy import Skype
import sys

# Variaveis -------------------------

# Dados de login do usuario
user = 'EMAIL'
passwd = 'SENHA'

# Instancia um objeto SkypeActions
sk = Skype(user, passwd)

# Pega todos os chats
chats = sk.chats.recent()

# Exibe a mensagem de boas vindas para o usuario
print("Seus chats:")
print("")

# Loop em chats
for chat in chats:
	try:
		# Printa o nome do grupo e o código
		print(chats[chat].topic, "=>", chat)
	except Exception as e:
		print("")


input("Aperte Enter para sair...")
sys.exit()
