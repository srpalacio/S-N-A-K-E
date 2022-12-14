import random
import pygame

class Food:
    
    def __init__(self):
        self.color=(222,0,0)
        self.x=0
        self.y=0
        self.size=10
        self.status="inactive"

    def putFood(self, x_max, y_max):
        #Generate a random x
        self.x=random.randint(0, x_max)
        self.y=random.randint(0, y_max)
        
                        
        if self.status=="inanctive":
            pygame.draw.rect(self.screen, self.food.color, (self.x,self.y,10,10))
            self.status="active"

        return(self.x, self.y)