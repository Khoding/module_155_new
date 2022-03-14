from sense_hat import SenseHat

import random, time


class CDormeur:
    def __init__(self, nom, color, line):
        self.nom = nom
        self.color = color
        self.line = line
        self.sleepyTime = random.randrange(2, 8, 1)

    def display(self, pos):
        print(pos)
        for i in range(8):
            if i < pos:
                sense.set_pixel(self.line, i, self.color)
            else:
                sense.set_pixel(self.line, i, (0, 0, 0))
        for i in range(pos, 8):
            sense.set_pixel(self.line, i, (0, 0, 0))

    def timeToSleep(self):
        print(self.nom + " s'endort . . . pour " + str(self.sleepyTime) + " secondes")
        for t in range(self.sleepyTime):
            time.sleep(1)
            self.display(self.sleepyTime - t - 1)
            print(self.sleepyTime - t)
        print(self.nom + " a fini de dormir et se réveille . . .")


noms = ["Roger", "Paul", "Lucie", "Sylvie", "Mathieu", "Pascal", "Aude", "Louis"]
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
dormeurs = []
sense = SenseHat()


def create_dormeurs():
    for n in noms:
        l = len(dormeurs)
        d = CDormeur(n, colors[l], l)
        dormeurs.append(d)


if __name__ == "__main__":
    sense.clear()
    create_dormeurs()

    for d in dormeurs:
        d.display(d.sleepyTime)

    for d in dormeurs:
        d.timeToSleep()
