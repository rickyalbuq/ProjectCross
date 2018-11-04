import sys, time, random
import pygame as pg

#Inicialização
def game_init(w, h):
	#Iniciar o Pygame
	pg.init()
	#Configs de Tela
	width, height = w, h
	size = width, height
	#Configs de Janela
	display = pg.display.set_mode(size)
	pg.display.set_caption("Cross The Road")
	return display

#Escolha Aleatoria de Sprite
def escolheObstaculo(cima, baixo):
	direcao = random.randint(0,1)
	if(direcao == 0):
		aux = random.randint(0,1)
		obstaculo = baixo[aux]
	else:
		aux = random.randint(0,1)
		obstaculo = cima[aux]
	return obstaculo, direcao

#Configs de Obstaculo
def posicaoInicial(obstaculo, direcao, pos_x):
	pos_y = 650
	pos_y_inverso = -50
	obstaculoRect = obstaculo.get_rect()
	if(direcao == 1):
		obstaculoRect.center = (pos_x,pos_y)
	else:
		obstaculoRect.center = (pos_x,pos_y_inverso)
	return obstaculoRect.center

#Sortear Pista
def tipoPista():
	tipo = random.randint(0,2)
	if(tipo == 0):
		pista = asfalto
	else:
		if(tipo == 1):
			pista = grama
		else:
			if(tipo == 2):
				pista = agua
	return pista, str(tipo)

#Distribuir Pistas na Grade
def geradorPista(pistas):
	x = 0
	for j in range(0,10):
		for i in range(0,6):	
			display.blit(pistas[j], (x,i*100))
		x+=80

#Movimento dos Obstaculos
def movObstaculo(obstaculoRect, direcao):
	#Movimento Carro Subindo
	pos_y -= random.randrange(10)
	pos_y_inverso += random.randrange(10)
	if(direcao == 1):
		if(pos_y <=-50):
			pos_y = 650
		obstaculoRect.center.y = pos_y
	else:
		if(pos_y_inverso >=650):
			pos_y_inverso = -50
			obstaculoRect.center.y = pos_y_inverso	
	return obstaculoRect.center

# --- Configs Iniciais --- #
display = game_init(800, 600)

#Carregar Sprites
asfalto       = pg.image.load("Sprites/asfalto.png")
agua          = pg.image.load("Sprites/agua.png")
grama         = pg.image.load("Sprites/grama.png")
carroCima     = pg.image.load("Sprites/carro_pra_cima.png")
carroBaixo    = pg.image.load("Sprites/carro_pra_baixo.png")
caminhaoCima  = pg.image.load("Sprites/caminhao_pra_cima.png")
caminhaoBaixo = pg.image.load("Sprites/caminhao_pra_baixo.png")
personagem    = pg.image.load("Sprites/player_01.png")

#Criar Listas
cima = [carroCima, caminhaoCima]
baixo = [carroBaixo, caminhaoBaixo]
ostaculosRect = []
obstaculos = []
direcoes = []
pistas = []
tipos = []

#Sortear as Pistas e Sprites (até o numero total de pistas)
for i in range(0,10):
	pistas, tipos = tipoPista()
	if(tipos[i]==0):
		pos_x = i*40
	obstaculos, direcoes = escolheObstaculo(cima, baixo)
	obstaculosRect = posicaoInicial(obstaculos[i], direcoes[i], pos_x)

# --- Loop Principal --- #
while True:

	#Loop de Eventos
	for event in pg.event.get():
		#Encerrar aplicação
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
	keys = pg.key.get_pressed()
	
	# --- Mostrar na Tela --- #

	#Gerar pistas
	geradorPista(pistas)

	#Loop de Mostrar Obstaculos
	for i in range(0, len(obstaculos)):
		display.blit(obstaculos[i],obstaculoRect[i])
		ostaculosRect = movObstaculo(obstaculosRect[i], direcoes[i])
		
	#Atualizar a Tela
	pg.display.flip()
	time.sleep(0.015)
