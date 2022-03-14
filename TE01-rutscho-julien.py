import subprocess, threading, time
from sense_hat import SenseHat


ping_objects = []


class CPingTest(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.reached = False
        self.ip = ip
        self.display(1)

    def test(self):
        print("ping de l'adresse {}".format(self.ip))
        ping_string = "ping %s -c 2" % self.ip  # Linux
        # ping_string = 'ping %s -n 2' % self.ip  # Windows
        ping_test = subprocess.call(ping_string, shell=True)
        if ping_test == 0:
            self.reached = True

    def display(self, pos):
        for i in range(8):
            if i < pos:
                sense.set_pixel(i, i, (255, 255, 255))
            else:
                sense.set_pixel(i, i, (255, 255, 255))
        for i in range(pos, 8):
            sense.set_pixel(i, i, (255, 255, 255))

    def run(self):
        self.start = time.time()
        self.test()
        tps2 = time.time()
        print("elapsed time = {0:.3f} s".format(tps2 - tps1))


def ping_test():
    global ping_objects
    num_reached = 0
    for i in range(1, 16, 1):
        ip = "10.224.96." + str(i)
        ping_objects.append(CPingTest(ip))

    for po in ping_objects:
        po.test()
        if po.reached:
            num_reached += 1

    return num_reached


sense = SenseHat()


if __name__ == "__main__":
    sense.clear()
    tps1 = time.time()
    n = ping_test()

    for po in ping_objects:
        po.start()

    while len(ping_objects) > 0:
        print("{} adresses ip détectées :".format(n))
        i = 0
        for po in ping_objects:
            i += 1
            if po.reached:
                print(po.ip)

        if i == len(ping_objects):
            break

    # tps2 = time.time()
    # print("elapsed time = {0:.3f} s".format(tps2 - tps1))
