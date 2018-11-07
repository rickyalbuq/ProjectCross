import sys, time, random
import pygame as pg

#Confis de Inicialização
def game_init(l, a):
	#Iniciar o Pygame
	pg.init()
	#Configs de Tela
	largura, altura = l, a
	tamanho = largura, altura
	estado = 0
	escolha = 9
	pontuacao = 0
	recorde = 0
	cont = 0
	#Configs de Janela
	tela = pg.display.set_mode(tamanho)
	pg.display.set_caption("Cross The Road")
	return tela, estado, cont, escolha, pontuacao, recorde

#Altera o estado atual
def mudancaEstado(estado, mousePressed, mousePosition, escolha, cont):
	if(estado == 0):
		if(mousePressed[0] == True):
			if(mousePosition > (300, 450) and mousePosition < (500, 486)):
				estado = 1
				cont = 0

	else:
		if(estado == 1):
			if(mousePressed[0] == True):
				if(mousePosition > (200, 250) and mousePosition < (280, 350)):
					escolha = 0
					estado = 2
					cont = 0

				else:
					if(mousePosition > (360, 250) and mousePosition < (420, 350)):
						escolha = 1
						estado = 2
						cont = 0

					else:	
						if(mousePosition > (520, 250) and mousePosition < (600, 350)):
							escolha = 2
							estado = 2
							cont = 0
		else:
			if(estado == 3):
				if(mousePressed[0] == True):
					if(mousePosition > (345, 400) and mousePosition < (450, 419)):
						estado = 2
						pontuacao = 0
						cont = 0

					else:
						if(mousePosition > (345, 470) and mousePosition < (450, 489)):
							estado = 1
							pontuacao = 0
							cont = 0

	return estado, escolha, cont

# --- Configs Resolução--- #
tela, estado, cont, escolha, pontuacao, recorde = game_init(800, 600)

# --- Loop Principal --- #
while True:
	#Loop de Eventos
	for event in pg.event.get():
		#Encerrar aplicação
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
	key = pg.key.get_pressed()[pg.K_RIGHT]
	keys = pg.key.get_pressed()
	mousePressed = pg.mouse.get_pressed()
	mousePosition = pg.mouse.get_pos()

	#Função de trocar estado
	estado, escolha, cont = mudancaEstado(estado, mousePressed, mousePosition, escolha, cont)
	
	# --- Mostrar na Tela --- #
	if(estado == 0):
		if(cont == 0):
			def menuPista(asfalto):
				x = 200
				for j in range(0,2):
					for i in range(0,8):	
						tela.blit(asfaltoMenu, (i*100, x))
					x += 80
			#Movimento dos carros do menu
			def movCarroMenu(obj1, obj2, esquerda, direita):
				esquerda -= random.randrange(20)
				direita  += random.randrange(20)
				obj1Rect  = obj1.get_rect()
				obj2Rect  = obj2.get_rect()
				obj1Rect  = (esquerda, 280)
				obj2Rect  = (direita, 200)
				if(esquerda < -100):
					esquerda = 900
				if(direita > 900):
					direita = -100
				return obj1Rect, obj2Rect, esquerda, direita

			logo             = pg.image.load("Sprites/logo.png")
			asfaltoMenu      = pg.image.load("Sprites/asfalto_lado.png")
			carroDireita     = pg.image.load("Sprites/carro_pra_direita.png")
			carroEsquerda    = pg.image.load("Sprites/carro_pra_esquerda.png")
			texto_menu       = pg.image.load("Sprites/texto_menu.png")
			autor            = pg.image.load("Sprites/autor.png")
			esquerda         = -100
			direita          = 900
			cont +=1

		#Gerar pistas
		menuPista(asfaltoMenu)
		#Mover Carros
		obj1Rect, obj2Rect, esquerda, direita = movCarroMenu(carroDireita, carroEsquerda, esquerda, direita)
		tela.blit(carroEsquerda, obj1Rect)
		tela.blit(carroDireita, obj2Rect)
		#Mostrar logo
		tela.blit(logo, (277, 160))
		#Mostrar textos
		tela.blit(texto_menu, (300, 450))
		tela.blit(autor, (345, 567))
		#Atualizar a Tela
		pg.display.flip()
		time.sleep(0.033)

	else:
		if(estado == 1):
			if(cont == 0):
				#Configs Iniciais
				bg      = pg.draw.rect(tela, (0,0,0), [0,0,800,600])
				player1 = pg.image.load("Sprites/player_01.png")
				player2 = pg.image.load("Sprites/player_02.png")
				player3 = pg.image.load("Sprites/player_03.png")

				fonte = pg.font.Font(None, 32)
				fonte2 = pg.font.Font(None, 20)
				colortext = (255,255,255)

				texto = fonte.render("Escolha seu personagem: ", True, colortext)
				nome1 = fonte.render("Ricky", True, colortext)
				nome2 = fonte.render("Ana", True, colortext)
				nome3 = fonte.render("Jorgiano", True, colortext)

				cont+= 1
				
			#Mostrar na tela
			tela.blit(player1, (200, 250))
			tela.blit(player2, (360, 250))
			tela.blit(player3, (520, 250))

			tela.blit(texto, (270, 160))
			tela.blit(nome1, (208, 360))
			tela.blit(nome2, (378, 360))
			tela.blit(nome3, (515, 360))	

			#Atualizar na tela
			pg.display.flip()
			time.sleep(0.033)
		else:
			if(estado == 2):
				if(cont == 0):
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
						pos_y = random.randrange(10)
						pos_y_inverso = random.randrange(10)
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
						return pista, tipo

					#Gera pistas na grade
					def geradorPista(pistas):
						x = 0
						for j in range(0,10):
							for i in range(0,6):	
								tela.blit(pistas[j], (x,i*100))
							x+=80

					#Config de Movimentação
					def movObstaculo(obstaculoRect, direcao, pos_y, pos_y_inverso):
						pos_y -= random.randrange(15)
						pos_y_inverso += random.randrange(15)
						if(direcao == 1):
							if(pos_y < -100):
								pos_y = 700
							aux = obstaculoRect[0]
							obstaculoRect = aux, pos_y
						else:
							if(direcao == 0):
								if(pos_y_inverso >= 700):
									pos_y_inverso = -100
								aux = obstaculoRect[0]
								obstaculoRect = aux, pos_y_inverso
						return obstaculoRect, pos_y, pos_y_inverso

					#Escolhe o Sprite do Personagem
					def escolherPersonagem(escolha):
						if(escolha == 0):
							personagem = player1
						else:
							if(escolha == 1):
								personagem = player2
							else:
								if(escolha == 2):
									personagem = player3
						return personagem

					#Dá a posição inicial do personagem
					def inicioPersonagem(personagem):
						play_pos_x = 0
						play_pos_y = 300
						personagemRect = personagem.get_rect()
						personagemRect.center = (play_pos_x, play_pos_y)
						return personagemRect.center, play_pos_x, play_pos_y

					#Movimenta a posição do personagem em relação a grade	
					def movPersonagem(personagemRect, play_pos_x, play_pos_y):
						if key:
							pg.key.set_repeat(0, 15)
							play_pos_x+= 80
							if(play_pos_x >720):
								play_pos_x = 720
						if keys[pg.K_UP]:
							play_pos_y-= 10
						if keys[pg.K_DOWN]:
							play_pos_y+= 10
						if(play_pos_y > 530):
							play_pos_y = 530
						else:
							if(play_pos_y < -30):
								play_pos_y = -30
						personagemRect = (play_pos_x, play_pos_y)
						return personagemRect, play_pos_x, play_pos_y

					#Detecta colisao entre personagem e objeto
					def colisao(personagemRect, obstaculosRect):
						player = pg.Rect(personagemRect, (80,100))
						for i in range(0, len(obstaculosRect)):
							objeto = pg.Rect(obstaculosRect[i], (80,100))
							if (player.colliderect(objeto)):
								estado = 3
								cont = 0
								break
							else:
								estado = 2
						return estado

					#Detecta colisao entre personagem e um troco
					def colisaoTronco(personagemRect, troncosRect):
						player = pg.Rect(personagemRect, (80,100))
						for i in range(0, len(troncosRect)):
							objeto = pg.Rect(troncosRect[i], (80,100))
							if (player.colliderect(objeto)):
								return troncosRect[i]
							else:
								return (0, 0)

					def geraTronco(pos_agua, aux_lista):
						for i in range(0, len(pos_agua)):
							aux_lista.append(random.randint(0,1))
							x = pos_agua[i]
							y = random.randrange(0,600)
							troncoRect = (x,y)
							troncosRect.append(troncoRect)
						return troncosRect, aux_lista

					def movTronco(troncoRect, aux):
						x = troncoRect[0]
						y = troncoRect[1]
						if(aux == 1):
							y += random.randint(0,10)
							if(y > 700):
								y = -100
							else:
								if(y < -100):
									y = 700
							troncoRect = (x, y)
						else:
							y -= random.randint(0,10)
							if(y > 700):
								y = -100
							else:
								if(y < -100):
									y = 700
							troncoRect = (x, y)

						return troncoRect

					def noTronco(personagemRect, troncoColidiu):
						x = personagemRect[0]
						y = troncoColidiu[1]
						personagemRect = (x, y)
						return personagemRect, x, y

					def marcarPontos(anterior, atual, pontuacao, recorde):
						if(anterior < atual):
							pontuacao+=1
							print("pontuação:", pontuacao)
						if(pontuacao > recorde):
							recorde = pontuacao
							print("recorde:", pontuacao)
						return pontuacao, recorde

					#Carregar Sprites
					asfalto       = pg.image.load("Sprites/asfalto.png")
					agua          = pg.image.load("Sprites/agua.png")
					grama         = pg.image.load("Sprites/grama.png")
					tronco        = pg.image.load("Sprites/tronco.png")
					carroCima     = pg.image.load("Sprites/carro_pra_cima.png")
					carroBaixo    = pg.image.load("Sprites/carro_pra_baixo.png")
					caminhaoCima  = pg.image.load("Sprites/caminhao_pra_cima.png")
					caminhaoBaixo = pg.image.load("Sprites/caminhao_pra_baixo.png")
					player1       = pg.image.load("Sprites/player_01.png")
					player2       = pg.image.load("Sprites/player_02.png")
					player3       = pg.image.load("Sprites/player_03.png")

					#Criar Listas
					cima                = [carroCima, caminhaoCima]
					baixo               = [carroBaixo, caminhaoBaixo]
					obstaculosRect      = []
					obstaculos          = []
					direcoes            = []
					pistas              = []
					tipos               = []
					pos_x_lista         = []
					play_pos_x_lista    = []
					pos_y_lista         = []
					pos_y_inverso_lista = []
					pos_agua            = []
					troncosRect         = []
					aux_lista           = []

					#Sortear as Pistas e Sprites (até o numero total de pistas)
					for i in range(0,10):
						a, b= tipoPista()
						pistas.append(a)
						tipos.append(b)
						if(tipos[i] == 0):
							pos_x_lista.append(i*80)
						if(tipos[i] == 2):
							pos_agua.append(i*80)
					for i in range(0, len(pos_x_lista)):
						c, d = escolheObstaculo(cima, baixo)
						obstaculos.append(c)
						direcoes.append(d)
						g, h, i = posicaoInicial(obstaculos[i], direcoes[i], pos_x_lista[i])
						obstaculosRect.append(g)
						pos_y_lista.append(h)
						pos_y_inverso_lista.append(i)

					#Gerar Troncos
					troncosRect, aux_lista = geraTronco(pos_agua, aux_lista)

					#Gerar Personagem
					personagem = escolherPersonagem(escolha)
					personagemRect, play_pos_x, play_pos_y = inicioPersonagem(personagem)
					play_pos_x_lista.append(play_pos_x)
					#Fim
					cont += 1

				#Gera pistas
				geradorPista(pistas)

				#Loop de Mostrar Obstaculos
				for i in range(0, len(obstaculos)):
					tela.blit(obstaculos[i], obstaculosRect[i])
					obstaculosRect[i], a, b = movObstaculo(obstaculosRect[i], direcoes[i], pos_y_lista[len(pos_y_lista) - 1], pos_y_inverso_lista[len(pos_y_inverso_lista) - 1])
					
					#Acrescenta uma nova posição e apaga uma antiga
					pos_y_lista.append(a)
					deleta = pos_y_lista[i]
					pos_y_lista.remove(deleta)
					pos_y_inverso_lista.append(b)
					deleta = pos_y_inverso_lista[i]
					pos_y_inverso_lista.remove(deleta)
				
				#Mover Troncos
				for i in range(0, len(troncosRect)):
					tela.blit(tronco, troncosRect[i])
					troncosRect[i] = movTronco(troncosRect[i], aux_lista[i])

				
				#Sobre a pontuação
				deleta = play_pos_x_lista[0]
				play_pos_x_lista.append(play_pos_x)
				#Contando pontuação
				pontuacao, recorde = marcarPontos(play_pos_x_lista[0], play_pos_x_lista[1], pontuacao, recorde)
				play_pos_x_lista.remove(deleta)

				#Verificar colisao
				estado  = colisao(personagemRect, obstaculosRect)
				troncoColidiu = colisaoTronco(personagemRect, troncosRect)

				#Mover o personagem
				
				#Mover o jogador junto do tronco
				if not(troncoColidiu == (0,0)):
					personagemRect, play_pos_x, play_pos_y = noTronco(personagemRect, troncoColidiu)
				personagemRect, play_pos_x, play_pos_y = movPersonagem(personagemRect, play_pos_x, play_pos_y)
				#Mostrar Personagem
				tela.blit(personagem, personagemRect)

				#Atualizar a Tela
				pg.display.flip()
				time.sleep(0.066)

			if(estado == 3):

				bg              = pg.draw.rect(tela, (0,0,0), [0,0,800,600])
				gameOver        = pg.image.load("Sprites/game_over.png")
				novamente       = pg.image.load("Sprites/novamente.png")
				mudarPersonagem = pg.image.load("Sprites/muda_personagem.png")
				texto = pontuacao
				pontuacao = 0

				#Mostrar logo
				tela.blit(gameOver, (277, 100))
				#Mostrar textos
				tela.blit(novamente, (345, 400))
				tela.blit(mudarPersonagem, (345, 470))
				#Atualizar a Tela
				pg.display.flip()
				time.sleep(0.033)
