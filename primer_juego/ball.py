import pygame
from random import randint


BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):

    def __init__(self, color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Dibujo la pelotita
        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.velocity = [0, 0]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-3,3)

    def paddle_bounce(self):
        self.velocity[1] = (-self.velocity[1])*1.5

    def go(self,level):
        self.velocity = [(8 + (level - 1 * 0.3)), (8 + (level - 1 * 0.3))]

