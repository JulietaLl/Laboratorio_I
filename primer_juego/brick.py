import pygame

BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        super().__init__()

        #Establezco color del ladrillo y su posición (x,y)
        #Pinto el fondo para que sea transparente


        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Dibujo el ladrillo
        pygame.draw.rect(self.image,color,[0,0,width, height])

        self.rect = self.image.get_rect()
    
   