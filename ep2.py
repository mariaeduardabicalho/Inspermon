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
					










