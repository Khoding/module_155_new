import subprocess
import time

ping_objects = []


class CPingTest:
    def __init__(self, ip):
        self.reached = False
        self.ip = ip

    def test(self):
        print("ping de l'adresse {}".format(self.ip))
        # ping_string = 'ping %s -c 2' % self.ip  # Linux
        ping_string = "ping %s -n 2" % self.ip  # Windows
        ping_test = subprocess.call(ping_string, shell=True)
        if ping_test == 0:
            self.reached = True


def ping_test():
    global ping_objects
    num_reached = 0
    for i in range(1, 12, 1):
        ip = "10.224.96." + str(i)
        ping_objects.append(CPingTest(ip))

    for po in ping_objects:
        po.test()
        if po.reached:
            num_reached += 1

    return num_reached


if __name__ == "__main__":
    tps1 = time.time()
    n = ping_test()
    print("{} adresses ip détectées :".format(n))
    for po in ping_objects:
        if po.reached:
            print(po.ip)

    tps2 = time.time()
    print("elapsed time = {0:.3f} s".format(tps2 - tps1))
