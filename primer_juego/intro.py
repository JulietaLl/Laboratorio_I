import pygame
import sys
import sqlite3
import pygame_textinput

GREENLITH = (61,74,87)
BLACK = (0,0,0)
FONT = "Consolas"

class intro():

    def __init__(self):

        #size = (800,600)
        self.surface = pygame.display.set_mode((800, 600))
        self.surface.fill(GREENLITH)
        self.font = pygame.font.match_font(FONT)
        self.clock = pygame.time.Clock()
        #menu_salutation = self.read_salutation()
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.menu()
        self.wait()
        
        
        #PRUEBA
    """def read_salutation(self):
        with sqlite3.connect("bd_btf.db") as conexion:
            try:
                results = conexion.execute("SELECT saludo FROM test ORDER BY saludo DESC LIMIT 1")
                return (results.fetchone())[0]

            except sqlite3.OperationalError as e:
                return str(e)


    def new_salutation(self, salutation):
        with sqlite3.connect("bd_btf.db") as conexion:
            try:
                new_salutation_message = (salutation,)
                conexion.execute("UPDATE test SET saludo = 'Holiwinski' WHERE saludo = 'Holiwis'")
                conexion.commit()
                return "insert_ok"

            except sqlite3.OperationalError as e:
                return str(e)
            """
    

    #pintar cualquier texto en la pantalla
    def display_text(self,text,size,color,pos_x,pos_y):
        font = pygame.font.Font(self.font,size)

        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        #self.surface.blit(text,rect)
        self.surface.blit(self.textinput.surface,(350,450))

    def menu(self):

        self.surface.fill(GREENLITH)
        self.display_text("BIENVENIDO HDP",36,BLACK, 400,300)

        pygame.display.flip()


        self.wait()
        
    def wait(self):
        
        wait = True 

        while wait:
            self.clock.tick()

            events = pygame.event.get()

            self.textinput.update(events)

            for event in events:
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYUP:
                    wait = False
