# Pack-Man		04/05/2020
# Author : Kevin Dufour

# Bibliothèque python pour faire des jeux 2D
import pygame
import random

# ================================================ OBJETS ==========================================================#

# Objet Rerésentant notre jeu 
class Game : 
	# Constructeur
	def __init__(self) :
		#
		self.player = Pacman()	# Contient notre joueur (Pacman Object)
		self.walls = []			# Contient les murs (obstacles de la partie, délimitation ...) (list)
		self.foods = []
		self.bonus = []
		self.ghosts = []
		self.create_map()

		self.image_death = [
			pygame.image.load('img/player/death/death-1.png'), pygame.image.load('img/player/death/death-2.png'),
			pygame.image.load('img/player/death/death-3.png'), pygame.image.load('img/player/death/death-4.png'),
			pygame.image.load('img/player/death/death-5.png'), pygame.image.load('img/player/death/death-6.png'),
			pygame.image.load('img/player/death/death-7.png'), pygame.image.load('img/player/death/death-8.png'),
			pygame.image.load('img/player/death/death-9.png'), pygame.image.load('img/player/death/death-10.png'),
			pygame.image.load('img/player/death/death-11.png'),
		]

	
	# Fonction permettant de créer la map de pacman
	def create_map(self) :
		# Contient les coordonées, la largeur et la hauteur des murs
		# Dans l'ordre on a :  x, y, width, height 
		propety_walls = [
			[160, 60, 380, 20 ],		# Mur du haut
			[160, 80, 20, 340],			# Mur de gauche
			[160, 420, 380, 20],		# Mur du bas
			[520, 80, 20, 340]			# Mur de droite
		]

		x = 160
		y = 60
		
		# La map de pacman
		self.maze = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 0, 0, 1, 0, 0, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 1, 0, 1, 0, 1, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 0, 1, 0, 1, 1, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 1, 1, 0, 0, 0, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 4, 1, 0, 1],
			[1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
			[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 4, 4, 1, 0, 1],
			[1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
		]

		# La map de pacman
		self.maze_clone = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 0, 0, 1, 0, 0, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 1, 0, 1, 0, 1, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 0, 1, 0, 1, 1, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 1, 1, 0, 0, 0, 0, 1, 9, 9, 1, 0, 1, 0, 0, 1, 0, 1],
			[1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 4, 1, 0, 1],
			[1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
			[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 4, 4, 1, 0, 1],
			[1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
		]

		# Modelisation des murs de délimitation
		rang_line = 0
		rang_case = 0
		for line in self.maze :
			for case in line :
				# On crée un mur si vaut 1
				if case == 1 :
					self.walls.append(Wall(x + rang_case, y + rang_line, 20, 20)) 
				elif case == 0 :
					self.foods.append(Food(x + rang_case, y + rang_line))
				elif case == 2 :
					self.bonus.append(Bonus(x + rang_case, y + rang_line))
				elif case == 3 :
					self.ghosts.append(Ghost("red", x + rang_case, y + rang_line))
				elif case == 4 :
					self.ghosts.append(Ghost("blue", x + rang_case, y + rang_line))
				elif case == 5 :
					self.ghosts.append(Ghost("pink", x + rang_case, y + rang_line))
				elif case == 6 :
					self.ghosts.append(Ghost("orange", x + rang_case, y + rang_line))
				# On change de case
				rang_case += 20
			# On change de ligne et on retourne au premier index des cases
			rang_line += 20
			rang_case = 0

# Objet Pacman (le joueur)
class Pacman(pygame.sprite.Sprite) :

	# Constructeur
	def __init__(self) :
		super().__init__()

		# Variables décrivant l'objet 
		self.x	= 180				# Coordonées x (int)
		self.y 	= 80				# Coordonées x (int)
		self.velocity = 10		# Vitesse de déplacement (int)
		self.invincible = False  # Définit si pacman peut manger es ghosts
		self.alive = True

		# Variables dérivant l'annimation de l'objet
		# if self.state % 2 == 0 => pacman-direction-1.png Else => pacman-direction-2.png
		self.state = 1											# Décrit l'état a afficher de pacman
		self.images = [
				pygame.image.load('img/player/pacman-down-1.png'), pygame.image.load('img/player/pacman-down-2.png'),	# index 0 et 1	=> DOWN
				pygame.image.load('img/player/pacman-up-1.png'), pygame.image.load('img/player/pacman-up-2.png'),		# index 2 et 3	=> UP
				pygame.image.load('img/player/pacman-right-1.png'), pygame.image.load('img/player/pacman-right-2.png'), # index 4 et 5	=> RIGHT
				pygame.image.load('img/player/pacman-left-1.png'), pygame.image.load('img/player/pacman-left-2.png'),	# index 6 et 8	=> LEFT
				pygame.image.load('img/player/pacman-0.png')															# index 9 persone neutre
			] # Les états de pacman en jeu
		self.image = self.images[self.state % 2]
		self.rect = self.image.get_rect()					# On récupère les propriétés du pacman
		self.rect.x = self.x								# Coordonées x de l'image (int)
		self.rect.y = self.y								# Coordonées y de l'image (int)

		# On definit les directions possible de pacman (right est la direction par defaut)
		self.direction = 4

	# Permet de déplacer le personnage vers le bas
	def move_down(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.y += self.velocity * multiple
		self.rect.y = self.y
		self.rect.x = self.x

	# Permet de déplacer le personnage vers le haut
	def move_up(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.y -= self.velocity * multiple
		self.rect.y = self.y
		self.rect.x = self.x

	# Permet de déplacer le personnage vers la gauche
	def move_left(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.x -= self.velocity * multiple
		self.rect.x = self.x
		self.rect.y = self.y

	# Permet de déplacer le personnage vers la droite
	def move_right(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.x += self.velocity * multiple
		self.rect.x = self.x
		self.rect.y = self.y



	# On change l'image à afficher
	def update_img(self) :
		self.image = self.images[self.direction + (self.state % 2)]
		self.rect = self.image.get_rect()

# Objet fantome (enemie)
class Ghost(pygame.sprite.Sprite) :
	# Constructeur
	def __init__(self, color, x, y) :
		super().__init__()

		# Variables décrivant l'objet 
		self.x	= x				# Coordonées x (int)
		self.y 	= y				# Coordonées x (int)
		self.velocity = 10		# Vitesse de déplacement (int)
		self.invincible = True   # Définit le ghost peut manger pacman
		self.eating = False		# Definit si le ghost est mangé
		self.init_x_position = x
		self.init_y_position = y

		if (color == "red") :
			# chargement des sprites du ghost rouge
			self.images = [
				pygame.image.load('img/ghost/red/ghost-down.png'),		# index 0 => DOWN
				pygame.image.load('img/ghost/red/ghost-up.png'),		# index 1 => UP
				pygame.image.load('img/ghost/red/ghost-right.png'),		# index 2 => RIGHT
				pygame.image.load('img/ghost/red/ghost-left.png'), 		# index 3 => LEFT
			] # Les états deu ghost en jeu

		elif(color == "blue") :
			# chargement des sprites du ghost bleu
			self.images = [
				pygame.image.load('img/ghost/blue/ghost-down.png'),		# index 0 => DOWN
				pygame.image.load('img/ghost/blue/ghost-up.png'),		# index 1 => UP
				pygame.image.load('img/ghost/blue/ghost-right.png'),	# index 2 => RIGHT
				pygame.image.load('img/ghost/blue/ghost-left.png'), 	# index 3 => LEFT
			] # Les états deu ghost en jeu

		elif(color == "pink") :
			# chargement des sprites du ghost rose
			self.images = [
				pygame.image.load('img/ghost/pink/ghost-down.png'),		# index 0 => DOWN
				pygame.image.load('img/ghost/pink/ghost-up.png'),		# index 1 => UP
				pygame.image.load('img/ghost/pink/ghost-right.png'),	# index 2 => RIGHT
				pygame.image.load('img/ghost/pink/ghost-left.png'), 	# index 3 => LEFT
			] # Les états deu ghost en jeu

		elif(color == "orange") :
			# chargement des sprites du ghost orange
			self.images = [
				pygame.image.load('img/ghost/orange/ghost-down.png'),		# index 0 => DOWN
				pygame.image.load('img/ghost/orange/ghost-up.png'),			# index 1 => UP
				pygame.image.load('img/ghost/orange/ghost-right.png'),		# index 2 => RIGHT
				pygame.image.load('img/ghost/orange/ghost-left.png'), 		# index 3 => LEFT
			] # Les états deu ghost en jeu

		self.image_eyes = [
			pygame.image.load('img/ghost/eyes/ghost-down.png'),			# index 0 => DOWN
			pygame.image.load('img/ghost/eyes/ghost-up.png'),			# index 1 => UP
			pygame.image.load('img/ghost/eyes/ghost-right.png'),		# index 2 => RIGHT
			pygame.image.load('img/ghost/eyes/ghost-left.png'), 		# index 3 => LEFT
		] # Les états deu ghost en jeu quand il est mangé

		self.image_scare = [
			pygame.image.load('img/ghost/ghost-scare-1.png'),			# index 0 => DOWN
			pygame.image.load('img/ghost/ghost-scare-1.png'),			# index 1 => UP
			pygame.image.load('img/ghost/ghost-scare-1.png'),			# index 2 => RIGHT
			pygame.image.load('img/ghost/ghost-scare-1.png'), 			# index 3 => LEFT
		] # Les états deu ghost en jeu quand il est pas invincible

		# On definit les directions possible de pacman (right est la direction par defaut)
		self.direction = 4
		self.last_direction = 4

		self.image = self.images[self.direction - 1]
		self.rect = self.image.get_rect()					# On récupère les propriétés du pacman
		self.rect.x = self.x								# Coordonées x de l'image (int)
		self.rect.y = self.y								# Coordonées y de l'image (int)

	# Permet de déplacer le personnage vers le bas
	def move_down(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.y += self.velocity * multiple
		self.rect.y = self.y
		self.rect.x = self.x

	# Permet de déplacer le personnage vers le haut
	def move_up(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.y -= self.velocity * multiple
		self.rect.y = self.y
		self.rect.x = self.x

	# Permet de déplacer le personnage vers la gauche
	def move_left(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.x -= self.velocity * multiple
		self.rect.x = self.x
		self.rect.y = self.y

	# Permet de déplacer le personnage vers la droite
	def move_right(self, multiple) :
		# On change les véritable coordonées et ensuite celle de l'imgage
		self.x += self.velocity * multiple
		self.rect.x = self.x
		self.rect.y = self.y

	# On change l'image à afficher
	def update_img(self) :
		self.image = self.images[game.player.direction - 1]
		self.rect = self.image.get_rect()

# Objet wall (osbtacle)
class Wall(pygame.sprite.Sprite) :
	# Constructeur
	def __init__(self, x, y, w, h) :
		super().__init__()

		self.color = (0,0,255)	# Couleur bleu
		self.truc = (88,88,255)	# Couleur bleu
		self.rect = pygame.Rect(x, y, w, h)

# Objet nourriture (petite)
class Food(pygame.sprite.Sprite) :
	# Constructeur
	def __init__(self, x, y) :
			super().__init__()

			self.image = pygame.image.load('img/food/normal_food.png')			# image de la food
			self.rect = self.image.get_rect()			# On récupère les propriétés du pacman
			self.rect.x = x
			self.rect.y = y

class Bonus(pygame.sprite.Sprite) :
	# Constructeur
	def __init__(self, x, y) :
			super().__init__()

			self.image = pygame.image.load('img/food/big_food.png')			# image de la food
			self.rect = self.image.get_rect()			# On récupère les propriétés du pacman
			self.rect.x = x
			self.rect.y = y

# ================================================ Fonctions ======================================================#

# Mange la nourriture
def eat_food(food) :
	global score
	game.foods.remove(food)		# supression de la nourriture
	score += 10					# Augmentation du score 10 points

# Permet de modifier les caractéristiques 
# des personnages lorsque pacman mange un bonus
def eat_bonus(bonus) :
	global score, timer_invincible
	game.bonus.remove(bonus) 	# Supression de la nourriture
	score += 50				    # Augmentation du score 50 points 
	timer_invincible = 0

	game.player.invincible = True

	for ghost in game.ghosts :
		if ghost.invincible == True :
			ghost.invincible = False
			ghost.image = ghost.image_scare[ghost.direction - 1]
			ghost.rect = ghost.image.get_rect()
			ghost.rect.x = ghost.x
			ghost.rect.y = ghost.y

# Permet de modifier les caractéristiques 
# des personnages lorsque pacman mange un bonus
def eat_pacman() :
	global life
	pygame.time.delay(1000)		# Petit delai
	game.player.alive = False
	i = 0
	life -=1
	while i < 11 :				# Tant que l'animation n'est pas terminé

		game.player.image = game.image_death[i]
		draw_game()		# On redessine le jeu figé 
		i+=1
		pygame.time.delay(300)
	# On reset les positions des éléments
	# Pour pacman 		
	game.player.x = 320
	game.player.y = 280

	# pour les ghosts 
	for i,ghost in enumerate(game.ghosts) :
		ghost.x = ghost.init_x_position
		ghost.y =  ghost.init_y_position
		end_path_random[i] = True

	game.player.alive = True
	pygame.time.delay(500)
# Permet de modifier les caractéristiques 
# des personnages lorsque pacman mange ghost
def eat_ghost(ghost) :
	global score
	score += 200	# Augmentation du score 50 points 

	ghost.eating = True
	ghost.image = ghost.image_eyes[ghost.direction - 1]

	# On utilise l'image convenable
	ghost.rect = ghost.image.get_rect()
	ghost.rect.x = ghost.x
	ghost.rect.y = ghost.y

# Dessine le jeu
def draw_game() :
	# Effacement du dessins précèdent
	screen.fill((0,0,0))

	# Création du nouveau dessin
	# Affichage de la map
	for wall in game.walls :
		pygame.draw.rect(screen, wall.color, wall.rect)

	# Affichage des foods
	for food in game.foods :
		screen.blit(food.image, food.rect)

	# Affichage des bonus
	for bonus in game.bonus :
		screen.blit(bonus.image, bonus.rect)

	# Affichage des ghosts
	for ghost in game.ghosts :
		screen.blit(ghost.image, ghost.rect)
		
	# Affihage de pacman (le joueur)
	if game.player.alive == True :
		screen.blit(game.player.image, game.player.rect)
		game.player.update_img()		# On rafraichi l'image stocké (en fonction de state)
	else : 
		screen.blit(game.player.image, game.player.rect)
		game.player.rect = game.player.image.get_rect()
		game.player.rect.x = game.player.x
		game.player.rect.y = game.player.y

	# MAJ de la fenêtre
	pygame.display.update()

# Permet d'analyser et de répondres aux évenements capturé
def event_procedure() :
	global comming_direction
	# On tente de capturer les évenements reçus (GESTION DES EVENEMENT)
	for event in pygame.event.get() :
		# Si le joueur ferme le jeu (la fenêtre)
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
		# Si on capture une touche de clavier enfoncée (Mouvement du player)
		elif event.type == pygame.KEYDOWN :	
			# Si on appui sur la flèche du bas
			if event.key == pygame.K_DOWN :
				comming_direction = 0

			# Si on appui sur la flèche du haut
			elif event.key == pygame.K_UP :
				comming_direction = 2

			# Si on appui sur la flèche de gauche
			elif event.key == pygame.K_LEFT :
				comming_direction = 6

			# Si on appui sur la flèche de droite
			elif event.key == pygame.K_RIGHT :
				comming_direction = 4

# Permet d'analyser les collisions dans le jeu et de faire les actions nécéssaires
def collision_procedure() :
	# Gestions des collisions avec la nourriture
	for food in game.foods :
		if food.rect.colliderect(game.player.rect) :
			# Pacman mange la nourriture
			eat_food(food)

	# Gestion des collisions avec les bonus
	for bonus in game.bonus :
		if bonus.rect.colliderect(game.player.rect) :
			# Pacman mange le bonus
			# Pacman deviens invincible et mange peut manger les ghost
			eat_bonus(bonus)

	# Gestion des collisions avec les ghosts
	for ghost in game.ghosts :
		if ghost.rect.colliderect(game.player.rect) :
			# Si le ghost n'est pas déja mangé 
			if ghost.eating == False :
				# Sois pacman se fait mangé, sois on mange le ghost
				if ghost.invincible == True :
					eat_pacman()
				elif ghost.invincible == False :
					eat_ghost(ghost)

	# Gestion des collision avec les murs
	wall_collision = False		# Indique si il y a une collision (elle se remet a False a chaque) tour de boucle
	for wall in game.walls :
		if wall.rect.colliderect(game.player.rect) :
			wall_collision = True

	if wall_collision == False :
		game.player.state += 1		# On change l'état de l'image
	# On constate qu'il y a une collision donc on fait revenir en arrière le personnage
	else : 
		if game.player.direction == 0 :				# DOWN
			game.player.move_up(1)

		elif game.player.direction == 2 :			# UP
			game.player.move_down(1)

		elif game.player.direction == 6 :			# LEFT
			game.player.move_right(1)

		elif game.player.direction == 4 :			# RIGHT
			game.player.move_left(1)

# Permet de gérer le temps d'execution de certaines actions
def timer_procedure() : 
	global timer_invincible, clock
	# Gestion de l'invincibilité de pacman
	if game.player.invincible == True :
		timer_invincible += clock.get_time()

		# On vérifie si 10 secondes ne c'est pas écoulé depuis que pacman est invincible
		# Si c'est le cas on arreter l'invincibilité de pacman
		if timer_invincible > 10000 :
			stop_invincible()

def stop_invincible() :
	game.player.invincible = False

	for ghost in game.ghosts :
		if ghost.eating == False :
			ghost.invincible = True
			ghost.image = ghost.images[ghost.direction - 1]

			# On utilise l'image convenable
			ghost.rect = ghost.image.get_rect()
			ghost.rect.x = ghost.x
			ghost.rect.y = ghost.y

# Recherche le plus ocourt chemin 

def pathfinding2(x_deb, y_deb, x_fin, y_fin) :
	x_deb -= 160
	y_deb -= 60
	x_fin -= 160
	y_fin -= 60

	mapCopy = game.maze
	for l, ligne in enumerate(mapCopy):
		for c, colonne in enumerate(ligne) :
			if colonne != 1 and colonne != 9 :
				# case walkable
				mapCopy[l][c] = 10000 # valeur max jamais dépassable en chemin

	# coordonnées pixel -> sommets
	squareX_ghost = int(x_deb//20)
	squareY_ghost = int(y_deb//20)
	squareX_player = int(x_fin//20)
	squareY_player = int(y_fin//20)

	squareToTest = []
	currSquareX = squareX_ghost
	currSquareY = squareY_ghost
	squareToTest.append([currSquareX, currSquareY])
	currentScore = 100
	mapCopy[currSquareY][currSquareX] = currentScore

	end = False
	while len(squareToTest) > 0 :

		for currSquare in squareToTest :
			currSquareX = currSquare[0]
			currSquareY = currSquare[1]
			currentScore = mapCopy[currSquareY][currSquareX]

			if (currSquareX == squareX_player) and currSquareY == squareY_player :
				end = True

			# A gauche ?
			if mapCopy[currSquareY][currSquareX-1] != 1 and mapCopy[currSquareY][currSquareX-1] != 9 :
				if currentScore+1 < mapCopy[currSquareY][currSquareX-1] :
					squareToTest.append([currSquareX-1, currSquareY])
					mapCopy[currSquareY][currSquareX-1] = currentScore+1

			# A bas ?
			if mapCopy[currSquareY+1][currSquareX] != 1 and mapCopy[currSquareY+1][currSquareX] != 9 :
				if currentScore+1 < mapCopy[currSquareY+1][currSquareX] :
					squareToTest.append([currSquareX, currSquareY+1])
					mapCopy[currSquareY+1][currSquareX] = currentScore+1

			# A droite ?
			if mapCopy[currSquareY][currSquareX+1] != 1 and mapCopy[currSquareY][currSquareX+1] != 9 :
				if currentScore+1 < mapCopy[currSquareY][currSquareX+1] :
					squareToTest.append([currSquareX+1, currSquareY])
					mapCopy[currSquareY][currSquareX+1] = currentScore+1

			# A haut ?
			if mapCopy[currSquareY-1][currSquareX] != 1 and mapCopy[currSquareY-1][currSquareX] != 9 :
				if currentScore+1 < mapCopy[currSquareY-1][currSquareX] :
					squareToTest.append([currSquareX, currSquareY-1])
					mapCopy[currSquareY-1][currSquareX] = currentScore+1


			squareToTest.remove(currSquare)

		if end == True :
			break

	currSquareX = squareX_player
	currSquareY = squareY_player
	currSquare = mapCopy[currSquareY][currSquareX]
	direction = -1
	path = []
	tempo = -1

	while currSquare > 100 :
		# A gauche  ( Si ce n'est pas un mur ou des cases inutiles à l'analyse )
		if mapCopy[currSquareY][currSquareX-1] != 1 and mapCopy[currSquareY][currSquareX-1] != 9 :
			# Si la valeur de la case est plus petite que celle dans la variable
			if mapCopy[currSquareY][currSquareX-1] < currSquare :
				tempo = mapCopy[currSquareY][currSquareX-1]
				tempo_currSquareY = currSquareY
				tempo_currSquareX =  currSquareX-1
				direction = 4

		# A bas  ( Si ce n'est pas un mur ou des cases inutiles à l'analyse )
		if mapCopy[currSquareY+1][currSquareX] != 1 and mapCopy[currSquareY+1][currSquareX] != 9 :
			#  SI la valeur de la case est plus petite que celle dans la variable
			if mapCopy[currSquareY+1][currSquareX] < currSquare :
				tempo = mapCopy[currSquareY+1][currSquareX]
				tempo_currSquareY = currSquareY+1
				tempo_currSquareX =  currSquareX
				direction = 2

		# A droite  ( Si ce n'est pas un mur ou des cases inutiles à l'analyse )
		if mapCopy[currSquareY][currSquareX+1] != 1 and mapCopy[currSquareY][currSquareX+1] != 9 :
			# Si la valeur de la case est plus petite que celle dans la variable
			if mapCopy[currSquareY][currSquareX+1] < currSquare :
				tempo = mapCopy[currSquareY][currSquareX+1]
				tempo_currSquareY = currSquareY
				tempo_currSquareX =  currSquareX+1
				direction = 6
		# A haut  ( Si ce n'est pas un mur ou des cases inutiles à l'analyse )
		if mapCopy[currSquareY-1][currSquareX] != 1 and mapCopy[currSquareY-1][currSquareX] != 9 :
			# Si la valeur de la case est plus petite que celle dans la variable
			if mapCopy[currSquareY-1][currSquareX] < currSquare :
				tempo = mapCopy[currSquareY-1][currSquareX]
				tempo_currSquareY = currSquareY-1
				tempo_currSquareX =  currSquareX
				direction = 0

		currSquare = tempo
		currSquareY = tempo_currSquareY
		currSquareX = tempo_currSquareX

		# On trace le chemin
		if direction == 0 : #UP
			path.append("DOWN")
			path.append("DOWN")
		
		elif direction == 2 : #DOWN
			path.append("UP")
			path.append("UP")
	
		elif direction == 4 : #LEFT
			path.append("RIGHT")
			path.append("RIGHT")
		
		elif direction == 6 : #RIGHT
			path.append("LEFT")
			path.append("LEFT")
			

	#print(path)
	return path

# Permet de gérer les mouvements des ghost
def mouvement_ghost() :
	for i, ghost in enumerate(game.ghosts) :
		# Si le ghost est invinible alors il peut manger pacman donc il va vers pacman 
		if ghost.invincible == True :
			rand = random.randint(0, 10)
			if rand < 10 and end_path_random[i] == True:
				go_pacman(ghost, i)
			else :
				go_random(ghost, i)

		# Si le ghost est mangé 
		elif ghost.invincible == False and ghost.eating == True :
			go_base(ghost, i)

		# Si notre ghost n'est plus invincible et qu'il n'est pas mangé
		elif ghost.invincible == False and ghost.eating == False :
			go_random(ghost, i)

# Permet de diriger les ghost vers le pacman
def go_pacman(ghost, i) :
	# Si le ghost est dans un carré de au coordonées au multiple de 20
	if ghost.x % 20 == 0 and ghost.y % 20 == 0 :
			path[i] = pathfinding2( ghost.x, ghost.y, game.player.x, game.player.y)

	# On fait bouger le ghost si il y a un chemin de disponible
	if len(path[i]) > 0 :
			moveTo = path[i][len(path[i]) - 1]

			if moveTo == "UP" :
				ghost.move_up(1)

			elif moveTo == "DOWN" :
				ghost.move_down(1)

			elif moveTo == "LEFT" :
				ghost.move_left(1)

			elif moveTo == "RIGHT" :
				ghost.move_right(1)

			# On supprime e dernier chemin car il est inutile
			del path[i][len(path[i]) - 1]

# Permet de diriger les ghost vers la base
def go_base(ghost, i) :
	# Si le ghost est dans un carré de au coordonées au multiple de 20
	if ghost.x % 20 == 0 and ghost.y % 20 == 0 :
			path[i] = pathfinding2( ghost.x, ghost.y, ghost.init_x_position, ghost.init_y_position)

	# On fait bouger le ghost si il y a un chemin de disponible
	if len(path[i]) > 0 :
			moveTo = path[i][len(path[i]) - 1]

			if moveTo == "UP" :
				ghost.move_up(1)

			elif moveTo == "DOWN" :
				ghost.move_down(1)

			elif moveTo == "LEFT" :
				ghost.move_left(1)

			elif moveTo == "RIGHT" :
				ghost.move_right(1)

			# On supprime e dernier chemin car il est inutile
			del path[i][len(path[i]) - 1]
	else :
		ghost.eating = False
		ghost.invincible = True
		ghost.image = ghost.images[ghost.direction - 1]

		# On utilise l'image convenable
		ghost.rect = ghost.image.get_rect()
		ghost.x = ghost.init_x_position
		ghost.y = ghost.init_y_position
		ghost.rect.x = ghost.x
		ghost.rect.y = ghost.y

# Permet de diriger les ghost de facon aléatoire
def go_random(ghost, i) :
	global end_path_random, x_rand, y_rand

	if end_path_random[i] == True :
		x_rand = random.randint(0, 18)
		y_rand = random.randint(0, 18)

		while game.maze_clone[y_rand][x_rand] != 0 :
			x_rand = random.randint(0, 18)
			y_rand = random.randint(0, 18)

		# Si le ghost est dans un carré de au coordonées au multiple de 20
		if ghost.x % 20 == 0 and ghost.y % 20 == 0 :
			path[i] = pathfinding2( ghost.x, ghost.y, (x_rand * 20 + 160), (x_rand * 20 + 60))

		end_path_random[i] = False

	# On fait bouger le ghost si il y a un chemin de disponible
	if len(path[i]) > 0 :
			moveTo = path[i][len(path[i]) - 1]

			if moveTo == "UP" :
				ghost.move_up(1)

			elif moveTo == "DOWN" :
				ghost.move_down(1)

			elif moveTo == "LEFT" :
				ghost.move_left(1)

			elif moveTo == "RIGHT" :
				ghost.move_right(1)

			# On supprime e dernier chemin car il est inutile
			del path[i][len(path[i]) - 1]
	else :
		end_path_random[i] = True

def save_movement() :
	# On on change les coordonées du pacman en fonction de sa direction (GESTION DE LA DIRECTION)
	#print(comming_direction)
	if comming_direction != game.player.direction and game.player.x % 20 == 0 and game.player.y % 20 == 0 :
		# On va vers la direction donné par l'utilisateur
		if comming_direction == 0 :				# DOWN
			game.player.move_down(2)

		elif comming_direction == 2 :			# UP
			game.player.move_up(2)

		elif comming_direction == 6 :			# LEFT
			game.player.move_left(2)

		elif comming_direction == 4 :			# RIGHT
			game.player.move_right(2)

		# On verifie si on est pas a la position d'un mur
		if game.maze_clone[(game.player.y - 60) // 20][(game.player.x  - 160) // 20] == 1 :
			# Retour en arrière car on est sur un mur
			if comming_direction == 0 :				# DOWN
				game.player.move_up(2)

			elif comming_direction == 2 :			# UP
				game.player.move_down(2)

			elif comming_direction == 6 :			# LEFT
				game.player.move_right(2)

			elif comming_direction == 4 :			# RIGHT
				game.player.move_left(2)

			# On va vers la direction du pacman 
			if game.player.direction == 0 :				# DOWN
				game.player.move_down(1)

			elif game.player.direction == 2 :			# UP
				game.player.move_up(1)

			elif game.player.direction == 6 :			# LEFT
				game.player.move_left(1)

			elif game.player.direction == 4 :			# RIGHT
				game.player.move_right(1)

		else : 
			# On va vers la direction donné par l'utilisateur
			if comming_direction == 0 :				# DOWN
				game.player.move_up(2)
				game.player.move_down(1)

			elif comming_direction == 2 :			# UP
				game.player.move_down(2)
				game.player.move_up(1)

			elif comming_direction == 6 :			# LEFT
				game.player.move_right(2)
				game.player.move_left(1)

			elif comming_direction == 4 :			# RIGHT
				game.player.move_left(2)
				game.player.move_right(1)
			game.player.direction = comming_direction

	else :

		if game.player.direction == 0 :				# DOWN
			game.player.move_down(1)

		elif game.player.direction == 2 :			# UP
			game.player.move_up(1)

		elif game.player.direction == 6 :			# LEFT
			game.player.move_left(1)

		elif game.player.direction == 4 :			# RIGHT
			game.player.move_right(1)
def game_over() :
	if len(game.bonus) == 0 and len(game.food) == 0 :
		# gagné
		print("gg")
		font = pygame.font.SysFont("comicsansms", 40)
		text = font.render("WIN", True, (0, 128, 0))
	elif life == 0 :
		# perdu
		print("lose")


# ======================================================================================================================#

# Initialisation du module d'affichage
pygame.init()

# Génération de la fenêtre de jeu
pygame.display.set_caption("Pac-Man","zuk.jpg")					# Titre de la fenêtre et son icone
screen = pygame.display.set_mode((720,480))							# On stock la fenêtre et on créer cces dimensions
score = 0
life = 2
timer_invincible = 1000000
clock = pygame.time.Clock()
path = [[], [], [], []]
rand_x = 0
rand_y = 0
end_path_random = [True, True, True, True]
comming_direction = 4

game = Game()		# Création d'une parite

# ================================================ BOUCLE DU JEU ======================================================#
run = True 
while run :
	# FPS
	clock.tick(10)

	draw_game()	# On dessine  le jeu

	if len(game.bonus) == 0 and len(game.foods) == 0 :
		# gagné
		print("gg")
		font = pygame.font.SysFont("comicsansms", 40)
		text = font.render("WIN", True, (0, 128, 0))
		textRect = text.get_rect()
		textRect.x = 320
		textRect.y = 230
		screen.blit(text, textRect)
		pygame.display.update()

		pygame.time.delay(5000)		# Petit delai

		# reset du jeu 
		score = 0
		life = 2
		timer_invincible = 1000000
		clock = pygame.time.Clock()
		path = [[], [], [], []]
		rand_x = 0
		rand_y = 0
		end_path_random = [True, True, True, True]
		comming_direction = 4

		game = Game()		# Création d'une parite

	elif life <= 0 :
		# perdu
		print("lose")
		font = pygame.font.SysFont("comicsansms", 40)
		text = font.render("LOSE", True, (128, 0, 0))
		textRect = text.get_rect()
		textRect.x = 320
		textRect.y = 230
		screen.blit(text, textRect)

		pygame.display.update()

		pygame.time.delay(5000)		# Petit delai

		# reset du jeu 
		score = 0
		life = 2
		timer_invincible = 1000000
		clock = pygame.time.Clock()
		path = [[], [], [], []]
		rand_x = 0
		rand_y = 0
		end_path_random = [True, True, True, True]
		comming_direction = 4

		game = Game()		# Création d'une parite
	else : 
		event_procedure() # GESTION des évenements
		save_movement()
		collision_procedure() # GESTION des collisions
		timer_procedure()	  # GESTION DU TEMPS DES ACTIONS
		mouvement_ghost()

