from Snake import Snake
from Food import Food
from Player import Player
import pygame

class Game:
    
    def __init__(self):
        self.snake=Snake()
        self.food=Food()
        self.player=Player()
        self.width=200
        self.height=200
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()
        self.fps=60

    def checkKeys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:self.fpst+=5
        elif keys[pygame.K_a]:self.fpst-=5
        elif keys[pygame.K_UP]:self.snake.direction="UP"
        elif keys[pygame.K_DOWN]:self.snake.direction="DOWN"
        elif keys[pygame.K_RIGHT]:self.snake.direction="RIGHT"
        elif keys[pygame.K_LEFT]:self.snake.direction="LEFT"
    
    def run(self):

        pygame.init()

        while self.snake.die()==True:
            self.clock.tick(self.fps)
            #Revisar los eventos y mirar si oprimen el botón cerrar
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            self.screen.fill((255,255,255))

            #Dibujar la serpiente

            for celda in self.snake.body:
                #Dibujar un rectángulo
                pygame.draw.rect(self.screen, self.snake.color, (celda[0],celda[1],10,10))              
            
            
            self.checkKeys()

            self.snake.move()
            
            self.food.putFood(self.width,self.height)

            pygame.display.flip()
            
myGame=Game()
myGame.run()