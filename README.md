# Project_Cross
Projeto da disciplina de Programação de Computadores. 2018.2

Certifique-se de ter a biblioteca Pygame instalada em sua maquina.
Para mais informações sobre a biblioteca acesse https://pygame.org.

----

## Documentação

### Funções:

1. *game_init*

   ```python
   def game_init(l, a):
       #Configs Iniciais
       tamanho = l, a
       #Iniciar o Pygame
       pg.init()
       #Configs de Janela
       tela = pg.display.set_mode(tamanho)
       pg.display.set_caption("Cross The Road")
       return tela
   ```

   **Descrição:**

   ​	Função que inicializa o Pygame, definem uma janela do Windows onde os eventos posteriores serão mostrados.

   **Utilização:**

   ```python
   tela = game_init(l, a)
   ```

   **Parâmetros:**

   ​	*`l`*: Recebe um inteiro referente a largura;

   ​	*`a`*: Recebe um inteiro referente a altura.

   **Retorno:**

   ​	*`tela`*: Retorna um objeto referente à janela criada.	


2. *menuPista*

   ```python
   #Gera as pistas do menu iniciar
   def menuPista(asfalto):
   	x = 200
   	for j in range(0,2):
   		for i in range(0,8):	
   			tela.blit(asfaltoMenu, (i*100, x))
   		x += 80
   ```

   **Descrição:**

   Função que mostra na tela do menu inicial duas linhas e sete colunas de sprites que simulam pistas.

   **Utilização:**

   ```python
   menuPista(asfalto)
   ```

   **Parâmetros:**

   ​	*`asfalto`*: Recebe um objeto referente a uma imagem.


3. *movCarroMenu*

   ```python
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
   ```

   **Descrição:**

   ​	Função que movimenta as sprites de automóveis para direita e para esquerda na tela do menu inicial, com velocidade aleatórias.
   **Utilização:**

   ```python
   obj1, obj2, esquerda, direita = movCarroMenu(obj1, obj2, esquerda, direita)
   ```
   
   **Parâmetros:**

   ​	*`obj1`:* Recebe um objeto referente a uma imagem de automóvel virado para esquerda;

   ​	*`obj2`:* Recebe um objeto referente a uma imagem de automóvel virado para direita;

   ​	*`direita`:* Recebe um inteiro referente a posição x do veiculo que se movimenta para a direita;

   ​	*`esquerda`:* Recebe um inteiro referente a posição x do veiculo que se movimenta para a esquerda.

   **Retorno:**

   ​	*`obj1Rect`:* Retorna uma tupla (x,y) referente a posição do obj1;

   ​	*`obj2Rect`:* Retorna uma tupla (x,y) referente a posição do obj2;

   ​	*`esquerda`:* Retorna um inteiro referente a nova posição x do veiculo que se movimenta para a esquerda;

   ​	*`direita`:* Retorna um inteiro referente a nova posição x do veiculo que se movimenta para a direita.
