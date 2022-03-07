from sense_hat import SenseHat,  ACTION_RELEASED
from numpy import random
from time import sleep
import _thread

sense = SenseHat()
numBalls = 0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


def ball(color, sleepingTime) :
    x = random.randint(4) + 1
    y = random.randint(4) + 1
    if x == y :
        x = x + 1 
    xdir = random.choice([-1, 1])
    ydir = random.choice([-1, 1])
    while True :
        sense.set_pixel(x, y, (0, 0, 0))
        x = x + xdir
        y = y + ydir
        #print(x, y)
        sense.set_pixel(x, y, color)        
        if x == 7 or x == 0 :
            xdir = xdir * -1
        if y == 7 or y == 0 :
            ydir = ydir * -1
        sleep(sleepingTime)

def add_ball() :
    global numBalls
    color = colors[numBalls%3]
    sleepTime = random.choice([0.05, 0.1, 0.15])
    _thread.start_new_thread(ball, (color, sleepTime))    
    numBalls = numBalls + 1
    print(str(numBalls) + " balls")

def new_ball(event) :
    if event.action != ACTION_RELEASED:
        add_ball()

sense.stick.direction_middle = new_ball

if __name__ == "__main__":
    sense.clear()
    for x in range (2) :
        add_ball()

    while True:
        pass

