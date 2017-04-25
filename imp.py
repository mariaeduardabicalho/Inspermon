import random
import json

def batalha()

nome=input('Qual é o seu nome?')

print('Olá,{0}! Bem vindo ao Inspérmon!'.format(nome))

print('Os personagens disponiveis  são:')

with open('inspermons.json','r') as inspermons:
	ips=json.load(inspermons)

with open('nomesinspermons.json','r') as nomesinspermons:
	nips=json.load(nomesinspermons)



for x in ips:
	print (x)
personagem=input('escolha seu companheiromon')

print('Seu personagem é {0}, agora vamos jogar!'.format(ips[0]['nome']))

while True:
	comando= input('você deseja dormir ou passear?')

	if comando.lower() =="dormir":
			niips_usuario[personagem]['vida']+=10
	#condicional de tempo

	if comando=="passear":
		adversario=random.choice(ips)
		nome_a =nips[adversario]['nome']
		vida_a =nips[adversario]['vida']
		escolha=input(print("Olha, você encontrou o {}! Deseja enfrentar (e) ou  tentar fugir (f)?". format(nome_a)))
		

		if escolha.lower()== "f":
			possibilidades=[certo, errado]
			resultado=random.choice(possibilidades)
			if resultado== "certo":
				continue
			else:
				print("A fuga deu errado, você perdeu sua chance de ataque! Se prepare para o ataque do adversario!")


		#if escolha.lower() == "e":




		if len(inspermons_usuario)>0:
			print(inspermons_usuario)
			nome_inspermon_usuario=input("escolha um pokemon para batalhar") #dici no dici, tentar fazer sem
			#inspermon_usuario=








#if comando== "comer"


