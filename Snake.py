
class Snake:

    def __init__(self):
        
        self.color=(0,0,225)
        self.direction="RIGHT"

        self.body=[(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0)]
    
    def updateCoordinates(self,x,y):
        if self.direction=="UP":
            y-=1
        elif self.direction=="DOWN":
            y+=1
        elif self.direction=="LEFT":
            x-=1
        elif self.direction=="RIGHT":
            x+=1

        return (x,y)

    def eat(self):

        for i in range (10):
            (x,y)=self.body[0]

            x,y =self.updateCoordinates(x,y)

            self.body.insert(0,(x,y))

    def move(self):
        #Ponerle la cabeza a la snake
        (x,y)=self.body[0]
        x,y =self.updateCoordinates(x,y)
        self.body.insert(0,(x,y))
        
        #Remove the tail
        self.body.pop()
        
    def die(self):
        
        control=True
        for i in range(self.body.__len__()-1):
        
                if self.body[0]==self.body[i+1]:
                    control=False
        return control
                