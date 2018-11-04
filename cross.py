import sys, time, random
import pygame as pg

#Confis de Inicialização
def game_init(l, a):
	#Iniciar o Pygame
	pg.init()
	#Configs de Tela
	largura, altura = l, a
	tamanho = largura, altura
	#Configs de Janela
	tela = pg.display.set_mode(tamanho)
	pg.display.set_caption("Cross The Road")
	return tela

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
	return obstaculoRect.center, pos_y, pos_y_inverso

#Escolhe de maneira aleatoria as pistas
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

#Gera pistas na grade
def geradorPista(pistas):
	x = 0
	for j in range(0,10):
		for i in range(0,6):	
			tela.blit(pistas[j], (x,i*100))
		x+=80

#Config de Movimentação
def movObstaculo(obstaculoRect, direcao, pos_y, pos_y_inverso):
	pos_y -= random.randrange(10)
	pos_y_inverso += random.randrange(10)
	if(direcao == 1):
		if(pos_y <=-50):
			pos_y = 650
		aux = obstaculoRect[0]
		obstaculoRect = aux, pos_y
	else:
		if(pos_y_inverso >=650):
			pos_y_inverso = -50
			aux = obstaculoRect[0]
			obstaculoRect = aux, pos_y_inverso	
	return obstaculoRect

# --- Configs Iniciais --- #
tela = game_init(800, 600)

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
obstaculosRect = []
obstaculos = []
direcoes = []
pistas = []
tipos = []

#Sortear as Pistas e Sprites (até o numero total de pistas)
for i in range(0,10):
	a, b= tipoPista()
	pistas.append(a)
	tipos.append(b)
	if(tipos[i] == 0):
		pos_x = i*40
	else:
		pos_x = -80
	c, d = escolheObstaculo(cima, baixo)
	obstaculos.append(c)
	direcoes.append(d)
	g, pos_y, pos_y_inverso = posicaoInicial(obstaculos[i], direcoes[i], pos_x)
	obstaculosRect.append(g)

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

	#Gera pistas
	geradorPista(pistas)

	#Loop de Mostrar Obstaculos
	for i in range(0, len(obstaculos)):
		tela.blit(obstaculos[i], obstaculosRect[i])
		obstaculosRect[i] = movObstaculo(obstaculosRect[i], direcoes[i], pos_y, pos_y_inverso)
		
	#Atualizar a Tela
	pg.display.flip()
	time.sleep(0.015)
