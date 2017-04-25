import random
import json
import time


def batalha1(aoud,vj,vo,pj,dj,po,do):
	fuga={}
	fuga['x']=aoud
	while vj>0 and vo>0:
		if fuga['x']== 'a':
			vo= vo-(pj-do)
			vj=vj-(po-dj)
		else:
			vj=vj-(po-dj)
			fuga['x']=='a'
	if vo<=0:
		insperdex.append(adversario)
		inspermons_usuario.append(adversario)
		return'Parabéns, você ganhou!'
	if vj<=0:
		return 'você perdeu!'
def batalha2(aoud,vj,vo):
	fuga={}
	l=list(range(100))
	fuga['x']=aoud
	while vj>0 and vo>0:

		if fuga['x']== 'a':
			k=random.choice(l)
			vj=vj-k+f4
		else:
			k=random.choice(l)
			vj=vj-k+f4
			z=random.choice(l)
			vo=vo-z

			fuga['x']=='a'

	if vo<=0:
		insperdex.append(adversario)
		inspermons_usuario.append(adversario)
		return'Parabéns, você ganhou!'
	if vj<=0:
		return 'você perdeu!'

def acharn(inspermon,l):
	for x in l:
		if x['nome'] == inspermon:
			return x['nome']
def achar(inspermon,l):
	for x in l:
		if x['nome'] == inspermon:
			return x

with open('inspermons.json','r') as inspermons:
	ips=json.load(inspermons)

with open('nomesinspad.json','r') as ainspermons:
	ladversarios=json.load(ainspermons)

insperdex= []
edr=0
f4=0

inspermons_usuario=ips

with open('djogadores.json','rb') as dici:
	dicionario_jogadores=json.load(dici)

nome=input('Qual é o seu nome? ')

print('Olá,{0}! Bem vindo ao Inspérmon!'.format(nome))
time.sleep(3)


if nome in dicionario_jogadores:
	inspermons_usuario=dicionario_jogadores[nome][0]
	f4=dicionario_jogadores[nome][1]
	personagem=dicionario_jogadores[nome][2]
	print('Seus inspermons eram:')
	for x in inspermons_usuario:
		print (x)
	time.sleep(2)
	print("Você tinha evoluido até a evolução " + str(f4))
	time.sleep(2)
	print("Seu coompanheiromon era "+ personagem)
	time.sleep(2)

print('Os personagens disponiveis  são: ')
for x in inspermons_usuario:
	print (x)


personagem=input('escolha seu companheiromon: ')


print('Seu personagem é {0}, agora vamos jogar!'.format(acharn(personagem,inspermons_usuario)))
time.sleep(2)

while True:

	inspdex=input("Para ver seu Insperdex digite 'i', para pular aperte enter")
	if inspdex == 'i':
			print(insperdex)
			time.sleep(2)

	f6=['o Luciano','a Camila','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar',]
	esc=random.choice(f6)
	
	if esc == 'jogar':
	
		comando= input('você deseja dormir ou passear? ' )

		if comando.lower() =="dormir":
			(achar(personagem,inspermons_usuario)['vida'])+=10

			print("agra sua vida é: "+str(achar(personagem,inspermons_usuario)['vida']))
			time.sleep(2)

		if comando=="passear":
			
			adversario=random.choice(ladversarios)
			nome_a =acharn(adversario,ladversarios)
			
			escolha=input(print("Olha, você encontrou o {}! Deseja enfrentar (e) ou  tentar fugir (f)? ".format(adversario['nome'])))

			

			if escolha.lower()== "f":
				possibilidades=['certo', 'errado']
				resultado=random.choice(possibilidades)
				if resultado== "certo":
					print("Parabéns, sua fuga deu certo!")
					continue

				else:

					print("A fuga deu errado, você perdeu sua chance de ataque!")	
					if len(inspermons_usuario)>0:
						ib=input( "Escolha um inspermon para batalhar: "+str(inspermons_usuario))
						print("você esolheu o {0}".format(achar(ib, inspermons_usuario)))
					
						if edr<=2:
							b=(batalha1('d',achar(ib,inspermons_usuario)['vida'],adversario['vida'],achar(ib,inspermons_usuario)['poder'],achar(ib,inspermons_usuario)['defesa'],adversario['poder'],adversario['defesa']))
							print(b)
							if b == 'Parabéns, você ganhou!':
								edr+=1

								print('Parabéns você passou de nível!')
						
						else:
							if b== 'Parabéns, você ganhou!':
								f4=f4*1.5
								
							print(batalha2('d',achar(ib,inspermons_usuario)['vida'],adversario['vida'],achar(ib,inspermons_usuario)['poder'],achar(ib,inspermons_usuario)['defesa'],adversario['poder'],adversario['defesa']))

			if escolha.lower()=='e':

				ib=input( "Escolha um inspermon para batalhar: "+str(inspermons_usuario))
				print("você esolheu o {0}".format(achar(ib, inspermons_usuario)))
				if edr<=2:
					b=batalha1('a',achar(ib,inspermons_usuario)['vida'],adversario['vida'],achar(ib,inspermons_usuario)['poder'],achar(ib,inspermons_usuario)['defesa'],adversario['poder'],adversario['defesa'])
					print(b)
					if b == 'Parabéns, você ganhou!':
						edr+=1
						if edr>2:
							print('Parabéns você passou de nível!')
				
				else:
					if b== 'Parabéns, você ganhou!':
							f4=f4*1.5
							
					print(batalha2('a',achar(ib,inspermons_usuario)['vida'],adversario['vida']))
		dicionario_jogadores[nome]=[inspermons_usuario,f4,personagem]
		with open("djogadores.json",'w') as dici:
			json.dump(dicionario_jogadores, dici)
	
	elif esc== 'Luciano' or 'Camila':
		esco=input("IH! {} te encontrou brincando de Inspermon no campus e quer te levar de volta para aula de Dsoft! Quer fugir para o fablab ou para o laboratorio 3?".format(esc))
		
		if esco.lower()=="fablab":
			p=['l','o','u','r','e','n','c','o']
			j=['@','#','%','&','*','^','~','_']
			print('HE HE HE....')
			time.sleep(2)
			print('Para entrar você tem que desvendar a forca!')
			time.sleep(2)
			print('DICA: momento insper')
			time.sleep(2)
			erro=3
			while p!=j:

				print(j)
				le=input('digite uma letra: ')
				if le in p:

					for x in range(len(p)):
						if p[x]==le:
							j[x]=p[x]			
				
				elif erro==1:
					print('Você perdeu suas chances! {} te capturou!'.format(esc))
					time.sleep(2)
					print('Adeus... HA HA HA >:D')
					exit()
				else:
					erro-=1
					print('Você errou! Agora restam mais {} chances de erro!'.format(erro))
			print(j)

		else:
			pal=['r','e','f','r','a','c','a','o']
			jo=['@','#','%','&','*','^','~','_']
			print('HE HE HE....')
			time.sleep(2)
			print('Para entrar você tem que desvendar a forca!')
			time.sleep(2)
			print('DICA: Óptica')
			time.sleep(2)
			erro=3
			while pal!=jo:
				print(jo)
				le=input('digite uma letra: ')
				if le in pal:

					for x in range(len(pal)):
						if pal[x]==le:
							jo[x]=pal[x]			
				
				elif erro==1:
					print('Você perdeu suas chances! {} te capturou!'.format(esc))
					time.sleep(2)
					print('Adeus... HA HA HA >:D')
					time.sleep(2)
					exit()
				else:
					erro-=1
					print('Você errou! Agora restam mais {} chances de erro!'.format(erro))
			print(jo)
		dicionario_jogadores[nome]=[inspermons_usuario,f4,personagem]
		with open("djogadores.json",'w') as dici:
			json.dump(dicionario_jogadores, dici)