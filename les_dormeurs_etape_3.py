from sense_hat import SenseHat
import random, time, datetime, threading

class CDormeur (threading.Thread) :
    def __init__(self, nom, color, line):
        threading.Thread.__init__(self)    
        self.nom = nom
        self.color = color
        self.line = line
        self.sleepyTime = random.randrange(2, 8, 1)
        self.display(self.sleepyTime)
        
    def display(self, pos) :
        for i in range(8) :
            if i < pos :
                sense.set_pixel(self.line, i, self.color)
            else :
                sense.set_pixel(self.line, i, (0, 0, 0))
        for i in range(pos, 8) :
            sense.set_pixel(self.line, i, (0, 0, 0))
        
    def timeToSleep(self) :
        for t in range (self.sleepyTime) :
            time.sleep(1)
            self.display(self.sleepyTime-t-1)
        
    def run(self) :
        self.start = time.time()
        self.timeToSleep()
        self.elapsedTime = time.time() - self.start    

noms = [ "Roger", "Paul", "Lucie", "Sylvie", "Mathieu", "Pascal", "Aude", "Louis"]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 128, 128),
          (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255) ]
dormeurs = []
sense = SenseHat()
timeFormat = "%H:%M:%S.%f"

def timeLocal() :
    t = datetime.datetime.utcnow()
    return t.strftime(timeFormat)

def create_dormeurs() :
    for n in noms :
        l = len(dormeurs)
        d = CDormeur(n, colors[l], l)
        dormeurs.append(d)
    random.shuffle(dormeurs)    

if __name__ == "__main__":
    sense.clear()
    create_dormeurs()
    
    messages = []
    
    messages.append(timeLocal() + " : Tout le monde va au lit")
    
    
    for d in dormeurs :
        d.start()
        messages.append(timeLocal() + " : " + d.nom + " se couche")
        #time.sleep(1/8)


    while len(dormeurs) > 0 :
        for i in range(len(dormeurs)) :
            if not dormeurs[i].is_alive() :
                text = "{0} : {1} se lève après {2:.3f} ({3:.3f})".format(timeLocal(), dormeurs[i].nom, dormeurs[i].elapsedTime, dormeurs[i].sleepyTime)
                messages.append(text)
                dormeurs.pop(i)
                break        
  
    messages.append(timeLocal() + " : Tout le monde est réveillé")

    for m in messages :
        #d.start()
        print(m)