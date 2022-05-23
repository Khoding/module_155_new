import random
import threading
import time

from sense_hat import SenseHat

primes = []
tps_tot = 0
nb_tot = 0

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
sense = SenseHat()


class Prime(threading.Thread):
    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.tps1 = 0.0
        self.tps2 = 0.0
        self.nb = 0
        self.start_time = begin
        self.end_time = end

    # Calcule si le nombre 'n' est premier
    def Isprime(self, n):
        if (n == 2) or (n == 3) or (n == 5):
            return True
        if (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0):
            return False
        i = 5
        d = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += d
            d = 6 - d
        return True

    # Calcule quels nombres sont premiers entre
    # self.start_time et self.end_time
    def IsPrimeRange(self):
        tps1 = time.time()
        nb = 0
        for n in range(self.start_time, self.end_time):
            if self.Isprime(n):
                nb += 1
        tps2 = time.time()
        return (tps2 - tps1), nb

    def run(self):
        global tps_tot, nb_tot
        tps, nb = self.IsPrimeRange()

        tps_tot += tps
        nb_tot += nb

        # Indique pour la tranche calculée, combien
        # de nombres premiers ont été trouvés, et le
        # temps nécessaire
        print("temps  = {0:.3f} s".format(tps))
        print(str(nb) + " nombres premiers trouvés")


def create_ranges():
    for k in range(0, nb_tranches):
        p = Prime(k * ecart, (k + 1) * ecart)
        primes.append(p)
    random.shuffle(primes)


if __name__ == "__main__":
    nb_tranches = 10
    nb_maximum = 2500000
    ecart = int(nb_maximum / nb_tranches)

    create_ranges()

    for p in primes:
        p.start()

    # while len(primes) > 0:
    #     for i in range(len(primes)):
    #         if not primes[i].is_alive():
    #             print("temps  = {0:.3f} s".format(primes[i].tps))
    #             print(str(primes[i].nb) + " nombres premiers trouvés")
    #             primes.pop(i)
    #             break

    # # Pour le nombre de traches de calcul demandées,
    # # calcule tranche après tranche, combien de
    # # nombres sont premiers
    # for k in range(0, nb_tranches):
    #     p = Prime(k * ecart, (k + 1) * ecart)
    #     tps, nb = p.IsPrimeRange()

    #     tps_tot += tps
    #     nb_tot += nb

    #     # Indique pour la tranche calculée, combien
    #     # de nombres premiers ont été trouvés, et le
    #     # temps nécessaire
    #     print("temps  = {0:.3f} s".format(tps))
    #     print(str(nb) + " nombres premiers trouvés")

    # Affiche un résumé des calculs
    print(
        "{0} itérations réalisées et {1} nombres premiers trouvés".format(
            nb_tranches, nb_tot
        )
    )
    print("Temps nécessaire {0:.3f} s".format(tps_tot))


# Tuples :
# https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
