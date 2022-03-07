from sense_hat import SenseHat,  ACTION_RELEASED
import threading
from numpy import random
from time import sleep

sense = SenseHat()
balls = []
numBalls = 0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class CBall(threading.Thread) :
    def __init__(self, color):
        threading.Thread.__init__(self)
        self.x = random.randint(4) + 1
        self.y = random.randint(4) + 1
        self.color = color
        if self.x == self.y :
            self.x = self.x + 1 
        self.xdir = random.choice([-1, 1])
        self.ydir = random.choice([-1, 1])
        
    def move(self) :
        sense.set_pixel(self.x, self.y, (0, 0, 0))
        self.x = self.x + self.xdir
        self.y = self.y + self.ydir
        sense.set_pixel(self.x, self.y, self.color)        
        if self.x == 7 or self.x == 0 :
            self.xdir = self.xdir * -1
        if self.y == 7 or self.y == 0 :
            self.ydir = self.ydir * -1
        sleep(0.1)

    def run(self):
        while True:
            self.move()

def add_ball() :
    global numBalls
    color = colors[numBalls%3]
    b = CBall(color)
    b.start()
    balls.append(b)
    numBalls = numBalls + 1
    print(str(len(balls)) + " balls")        

def new_ball(event) :
    if event.action != ACTION_RELEASED:
        add_ball()

sense.stick.direction_middle = new_ball

if __name__ == "__main__":
    sense.clear()
    add_ball()

    while True:
        pass
   
