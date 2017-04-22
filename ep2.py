import random
import json


insperdex= []
edr=0
f4=0

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
	#[element for element in ips if element['nome'] == personagem]
	#if caract== 'nome':
	for x in l:
		if x['nome'] == inspermon:
			return x['nome']
def achar(inspermon,l):
	for x in l:
		if x['nome'] == inspermon:
			return x







nome=input('Qual é o seu nome? ')

print('Olá,{0}! Bem vindo ao Inspérmon!'.format(nome))

print('Os personagens disponiveis  são:')

with open('inspermons.json','r') as inspermons:
	ips=json.load(inspermons)



with open('nomesinspad.json','r') as ainspermons:
	ladversarios=json.load(ainspermons)


#with open('nomesinspermons.json','r') as nomesinspermons:
	#nips=json.load(nomesinspermons)
for x in ips:
	print (x)

inspermons_usuario=ips
personagem=input('escolha seu companheiromon: ')


print('Seu personagem é {0}, agora vamos jogar!'.format(acharn(personagem,ips)))




while True:
	
	inspdex=input("Para ver seu Insperdex digite 'i', para pular aperte enter")
	if inspdex == 'i':
		print(insperdex)


	comando= input('você deseja dormir ou passear?' )

	if comando.lower() =="dormir":
		(achar(personagem,ips)['vida'])+=10

		print("agra sua vida é: "+str(achar(personagem,ips)['vida']))

	if comando=="passear":
		#print(ladversarios)
		adversario=random.choice(ladversarios)
		
		nome_a =acharn(adversario,ladversarios)
		#vida_a =(achar(adversario,ladversarios)['vida'])
		escolha=input(print("Olha, você encontrou o {}! Deseja enfrentar (e) ou  tentar fugir (f)? ". format(adversario['nome'])))

		

		if escolha.lower()== "f":
			possibilidades=['certo', 'errado']
			resultado=random.choice(possibilidades)
			if resultado== "certo":
				continue

			else:

				print("A fuga deu errado, você perdeu sua chance de ataque!")	
				if len(inspermons_usuario)>0:
					ib=input( "Escolha um inspermon para batalhar: "+str(inspermons_usuario))
					print("você esolheu o {0}".format(achar(ib, ips)))
				
				if edr<=2:
					b=(batalha1('d',achar(ib,ips)['vida'],adversario['vida'],achar(ib,ips)['poder'],achar(ib,ips)['defesa'],adversario['poder'],adversario['defesa']))
					print(b)
					if b == 'Parabéns, você ganhou!':
						edr+=1

							print('Parabéns você passou de nível!')
				
				else:
					if b== 'Parabéns, você ganhou!':
						f4=f4*1.5
						
					print(batalha2('d',achar(ib,ips)['vida'],adversario['vida'],achar(ib,ips)['poder'],achar(ib,ips)['defesa'],adversario['poder'],adversario['defesa']))

		if escolha.lower()=='e':

			ib=input( "Escolha um inspermon para batalhar: "+str(inspermons_usuario))
			print("você esolheu o {0}".format(achar(ib, ips)))
			if edr<=2:
				b=batalha1('a',achar(ib,ips)['vida'],adversario['vida'],achar(ib,ips)['poder'],achar(ib,ips)['defesa'],adversario['poder'],adversario['defesa'])
				print(b)
				if b == 'Parabéns, você ganhou!':
					edr+=1
					if x>2:
						print('Parabéns você passou de nível!')
			
			else:
				if b== 'Parabéns, você ganhou!':
						f4=f4*1.5
						
				print(batalha2('a',achar(ib,ips)['vida'],adversario['vida']))
					import random
import json
import time

insperdex= []
edr=0
f4=0

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

nome=input('Qual é o seu nome? ')

print('Olá,{0}! Bem vindo ao Inspérmon!'.format(nome))
time.sleep(3)
print('Os personagens disponiveis  são: ')

with open('inspermons.json','r') as inspermons:
	ips=json.load(inspermons)

with open('nomesinspad.json','r') as ainspermons:
	ladversarios=json.load(ainspermons)

for x in ips:
	print (x)

inspermons_usuario=ips
time.sleep(2)
personagem=input('escolha seu companheiromon: ')


print('Seu personagem é {0}, agora vamos jogar!'.format(acharn(personagem,ips)))
time.sleep(2)

while True:

	inspdex=input("Para ver seu Insperdex digite 'i', para pular aperte enter")
	if inspdex == 'i':
			print(insperdex)
			time.sleep(2)

	f6=['Luciano','Camila','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar','jogar',]
	esc=random.choice(f6)
	
	if esc == 'jogar':
	
		comando= input('você deseja dormir ou passear? ' )

		if comando.lower() =="dormir":
			(achar(personagem,ips)['vida'])+=10

			print("agra sua vida é: "+str(achar(personagem,ips)['vida']))
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
						print("você esolheu o {0}".format(achar(ib, ips)))
					
						if edr<=2:
							b=(batalha1('d',achar(ib,ips)['vida'],adversario['vida'],achar(ib,ips)['poder'],achar(ib,ips)['defesa'],adversario['poder'],adversario['defesa']))
							print(b)
							if b == 'Parabéns, você ganhou!':
								edr+=1

								print('Parabéns você passou de nível!')
						
						else:
							if b== 'Parabéns, você ganhou!':
								f4=f4*1.5
								
							print(batalha2('d',achar(ib,ips)['vida'],adversario['vida'],achar(ib,ips)['poder'],achar(ib,ips)['defesa'],adversario['poder'],adversario['defesa']))

			if escolha.lower()=='e':

				ib=input( "Escolha um inspermon para batalhar: "+str(inspermons_usuario))
				print("você esolheu o {0}".format(achar(ib, ips)))
				if edr<=2:
					b=batalha1('a',achar(ib,ips)['vida'],adversario['vida'],achar(ib,ips)['poder'],achar(ib,ips)['defesa'],adversario['poder'],adversario['defesa'])
					print(b)
					if b == 'Parabéns, você ganhou!':
						edr+=1
						if x>2:
							print('Parabéns você passou de nível!')
				
				else:
					if b== 'Parabéns, você ganhou!':
							f4=f4*1.5
							
					print(batalha2('a',achar(ib,ips)['vida'],adversario['vida']))
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











