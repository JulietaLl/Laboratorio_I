
import pygame
import pygame_textinput
import os
from paddle import Paddle
from ball import Ball
from brick import Brick
from random import randint
from User import User
from new_intro import*
from ranking_reader import*
from ranking_output import*



pygame.init()

intro_manager = NewIntro()

current_user = User(intro_manager.inputted_text)

dir_name = os.path.dirname(__file__)
dir_sounds = os.path.join(dir_name,"Sonidos")

"""
ranking_reader = RankingReader()
ranking_parser = RankingOutput()

top_three_tuple_list = ranking_reader.readTopThree()
parsed_str = ranking_parser.parse_tuple_list(top_three_tuple_list)

print(parsed_str)"""

#Pruba Ingresar usuario nuevo
"""user = User("Nacho")
print(user)
"""
#intro_manager = intro()
#intro_manager.new_salutation("a")


#DEFINICIÓN DE COLORES

WHITE = (255,255,255)
DARKBLUE = (36,90,190)
RED = (255,0,0)
LITHBLUE = (0,176,240)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
ROSA = (218,144,175)
VIOLET = (146,121,210)
DARK = (28,61,84)
HEX = (117,209,198)
SOFTRED = (210,121,161)
SKY = (125,170,212)
BEIGE = (46,101,138)
GREENLITH = ()

score = 0
lives = 3
level = 1

# Nueva ventana 
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brekout Game")

icono = pygame.image.load("Icono_2.png")
pygame.display.set_icon(icono)

#Esta es la lista que contiene todos los sprites que se usan en el juego!
all_sprites_list = pygame.sprite.Group()

#Creación del paddle
paddle = Paddle(LITHBLUE,100,10)
paddle.rect.x = 350
paddle.rect.y = 560

#Creación de la pelotita
ball = Ball(WHITE,10,10)
ball.rect.x = 350 + (paddle.image.get_width() / 2) - (ball.image.get_width() / 2)
ball.rect.y = 550

all_bricks = pygame.sprite.Group()

for i in range(7):
    brick = Brick(SKY,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(VIOLET,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(HEX,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ROSA,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)



#Acá agrego la pelotita y el paddle a la lista de sprites!
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

#El reloj se va a detener cuando el usuario salga del juego.
clock = pygame.time.Clock()

carry_on = True

#----------- Main Program loop ------------------------------------#

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False

# El movimiento del paddle cuando el usuario usa alguna de las flechas

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(10)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(10)
    if keys[pygame.K_SPACE] and ball.velocity[0] == 0 and ball.velocity[1] == 0:
        ball.go(level)

#----- Logica del juego  acá -----# 
    all_sprites_list.update()

# Comprueba si la pelota rebota contra alguna de las paredes 

    if ball.rect.x >= 790 or ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        if ball.velocity[1] >= -1 and ball.velocity[1] <= 1:
            ball.velocity[1] = (ball.velocity[1] + 0.1) * 2
    if ball.rect.y >= 590:
        ball.velocity[1] = -ball.velocity[1]
        sound = pygame.mixer.Sound(os.path.join(dir_sounds,"wrong.mp3"))
        sound.play()
        lives -= 1
        if lives == 0:

            sound = pygame.mixer.Sound(os.path.join(dir_sounds,"game_over.wav"))
            sound.play()

            #Cuando el usuario pierde se muestra el mensaje
            #GAME OVER" durante 3 segundos y se muestra el Ranking de los primeros 3 puestos
            current_user.update_score(score)

            ranking_reader = RankingReader()
            tuple_list = ranking_reader.readTopThree()
            string_ranking = RankingOutput()
            parsed_str = string_ranking.parse_tuple_list(tuple_list)

            top_one = string_ranking.parse_top_one(tuple_list)
            top_two = string_ranking.parse_top_two(tuple_list)
            top_three = string_ranking.parse_top_three(tuple_list)


            
            font = pygame.font.Font(None,70)
            text = font.render("GAME OVER",1,WHITE)
            screen.blit(text,(268,300))

            font_2 = pygame.font.Font(None,30)
            text_2 = font_2.render(top_one,1,WHITE)
            screen.blit(text_2,(320,375))

            font_3 = pygame.font.Font(None,30)
            text_3 = font_2.render(top_two,1,WHITE)
            screen.blit(text_3,(320,405))

            font_4 = pygame.font.Font(None,30)
            text_4 = font_2.render(top_three,1,WHITE)
            screen.blit(text_4,(320,435))

            pygame.display.flip()
            pygame.time.wait(30000)
            


            # Se detiene el juego
            carry_on = False

    if ball.rect.y <= 40:
        ball.velocity[1] = -ball.velocity[1]
        if ball.velocity[0] >= -1 and ball.velocity[0] <= 1:
            ball.velocity[0] = (ball.velocity[0] + 0.1) * 2

    # Acá detecta colisiones entre la pelota y el paddle

    if pygame.sprite.collide_mask(ball,paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.paddle_bounce()

    # Detecta si la pelotita choca con algún ladrillo

    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    
    for brick in brick_collision_list:

        ball.bounce()
        score += 1
        brick.kill()

        sound = pygame.mixer.Sound(os.path.join(dir_sounds,"260614__kwahmah_02__pop.wav"))
        sound.play()

        if len(all_bricks) == 0:
            level +=1

            #Si el usuario rompe todos los ladrillos = pasa de nivel
            # y se muestra el mensaje de "Level Complete" durante 3 segundos 

            font = pygame.font.Font(None,60)
            text = font.render("LEVEL COMPLETE",1,WHITE)
            screen.blit(text,(200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Se reinicia la posición del paddle y la pelotita
          

            paddle.rect.x = 350
            paddle.rect.y = 560

            ball.rect.x = 350 + (paddle.image.get_width() / 2) - (ball.image.get_width() / 2)
            ball.rect.y = 550
                    
            ball.velocity[0] = 0
            ball.velocity[1] = 0

            # Se dibujan ladrillos aleatorios cada vez que comienza un nivel

            new_bricks = randint(3, 7)
            for i in range(new_bricks):
                brick = Brick(SOFTRED,80,30)
                brick.rect.x = (60 * (7-new_bricks+1)) + i* 100
                brick.rect.y = 60
                all_sprites_list.add(brick)
                all_bricks.add(brick)
            
            new_bricks = randint(4, 7)
            for i in range(new_bricks):
                brick = Brick(VIOLET,80,30)
                brick.rect.x = (60 * (7-new_bricks+1)) + i* 100
                brick.rect.y = 100
                all_sprites_list.add(brick)
                all_bricks.add(brick)

            new_bricks = randint(5, 7)
            for i in range(new_bricks):
                brick = Brick(HEX,80,30)
                brick.rect.x = (60 * (7-new_bricks+1)) + i* 100
                brick.rect.y = 140
                all_sprites_list.add(brick)
                all_bricks.add(brick)

            new_bricks = randint(4, 7)
            for i in range(new_bricks):
                brick = Brick(ROSA,80,30)
                brick.rect.x = (60 * (7-new_bricks+1)) + i* 100
                brick.rect.y = 180
                all_sprites_list.add(brick)
                all_bricks.add(brick)

            new_bricks = randint(3, 7)
            for i in range(new_bricks):
                brick = Brick(VIOLET,80,30)
                brick.rect.x = (60 * (7-new_bricks+1)) + i* 100
                brick.rect.y = 220
                all_sprites_list.add(brick)
                all_bricks.add(brick)


            new_bricks = randint(2, 7)
            for i in range(new_bricks):
                brick = Brick(SKY,80,30)
                brick.rect.x = (60 * (7-new_bricks+1)) + i* 100
                brick.rect.y = 260
                all_sprites_list.add(brick)
                all_bricks.add(brick)
                #carry_on = False

# --  Acá se ubica el código donde se dibuja! 
# Primero pinto la pantalla de color : Celeste Oscuro

    screen.fill(DARK)

    #Dibujo la linea que se para el texto del juego
    pygame.draw.line(screen , WHITE, [0,38], [800,38],2)

 # Muestra la puntuación y el número de vidas en la parte superior de la pantalla

    font = pygame.font.Font(None,34)
    text = font.render("Score: " + str(score), 1 , WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives),1, WHITE)
    screen.blit(text, (650,10))
    text = font.render("Level: " + str(level),1, WHITE)
    screen.blit(text, (350,10))

    # Se dibujan los sprites

    all_sprites_list.draw(screen)
    
    # Actualiza la pantalla 
    pygame.display.flip()

# 60 fotogramas por segundo
    clock.tick(60)

pygame.quit()







