import random
import threading
import time

from sense_hat import SenseHat

sense = SenseHat()
balls = []
numBalls = 0

pos = 0


class CDormeur:
    def __init__(self, nom):
        global pos
        self.nom = nom
        self.sleepyTime = random.randrange(1, 8, 1)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.pos = pos
        pos += 1

    def timeToSleep(self):
        print(self.nom + " s'endort pour " + str(self.sleepyTime) + " secondes")
        for i in range(0, self.sleepyTime):
            sense.set_pixel(i, self.pos, self.color)
        reversed_range = range(self.sleepyTime, -1, -1)
        for i in reversed_range:
            sense.set_pixel(i, self.pos, (0, 0, 0))
            time.sleep(1)
        print(self.nom + " a fini de dormir et se reveille...")


noms = ["Roger", "Paul", "Lucie", "Sylvie", "Mathieu", "Pascal", "Aude", "Louis"]
dormeurs = []


if __name__ == "__main__":
    sense.clear()

    for n in noms:
        d = CDormeur(n)
        dormeurs.append(d)

    for d in dormeurs:
        itsTimeToWakeUp = threading.Thread(target=d.timeToSleep, args=())
        itsTimeToWakeUp.start()
