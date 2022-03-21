import random
import threading
from time import sleep

from sense_hat import SenseHat

sense = SenseHat()


class Race(threading.Thread):
    """Race class"""

    def __init__(self):
        threading.Thread.__init__(self)


class Contestants:
    def __init__(self, nom, posx, posy):
        self.nom = nom
        self.posx = posx
        self.posy = posy

    def display(self):
        for i in range(8):
            if i < self.posx:
                sense.set_pixel(0, self.posy, (255, 255, 255))
            else:
                sense.set_pixel(self.posy, 0, (255, 255, 255))
        for i in range(self.posx, 8):
            sense.set_pixel(self.posx, 0, (255, 255, 255))

    def forward_fast(self):
        self.posx = self.posx + 3

    def slide(self):
        self.posx = self.posx - 6

    def big_slide(self):
        self.posx = self.posx - 12

    def small_slide(self):
        self.posx = self.posx - 2

    def forward_slow(self):
        self.posx = self.posx + 1

    def sleep(self):
        self.posx = self.posx

    def big_jump(self):
        self.posx = self.posx + 9

    def small_jump(self):
        self.posx = self.posx + 1

    def rand_movement_turtle(self):
        i = random.randrange(1, 10)
        if i >= 1 or i <= 5:
            c.forward_fast()
        elif i >= 6 or i <= 7:
            c.slide()
        else:
            c.forward_slow()

    def rand_movement_hare(self):
        i = random.randrange(1, 10)
        if i >= 1 or i <= 2:
            c.sleep()
        if i >= 3 or i <= 4:
            c.big_jump()
        if i == 5:
            c.big_slide()
        elif i >= 6 or i <= 8:
            c.small_jump()
        else:
            c.small_slide()


colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (128, 128, 128),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 255),
]


contestants_names = ["Hare", "Turtle"]

contestants = []


def create_contestants():
    for name in contestants_names:
        c = Contestants(name, 0, 0)
        contestants.append(c)


if __name__ == "__main__":
    sense.clear()
    create_contestants()

    for c in contestants:
        c.display()

    sleep(1)

    while range(3):
        for c in contestants:
            if c == contestants[0]:
                contestants[0].rand_movement_hare()
            else:
                contestants[1].rand_movement_turtle()
            c.display()
        sleep(1)
