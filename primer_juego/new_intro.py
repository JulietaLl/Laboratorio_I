import pygame
import pygame_textinput

class NewIntro():

    def __init__(self):
        
        # Creo el objeto de entrada de texto
        textinput = pygame_textinput.TextInputVisualizer()

        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Brekout Game")
        icono = pygame.image.load("Icono_2.png")
        pygame.display.set_icon(icono)
        clock = pygame.time.Clock()

        continue_looping = True

        while continue_looping:
            
            screen.fill((255,255,255))

            events = pygame.event.get()

            textinput.update(events)

            font = pygame.font.Font(pygame.font.match_font("Consolas"),20)

            text = font.render("Ingrese su nombre de usuario: ", True, (0,0,0))
            rect = text.get_rect()
            rect.midtop = (10, 10)

            #self.surface.blit(text,rect)
            screen.blit(text,(245,190))
            
            
            screen.blit(textinput.surface, (245, 235))

            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.inputted_text = textinput.value
                    continue_looping = False

            pygame.display.update()

            clock.tick(30)

