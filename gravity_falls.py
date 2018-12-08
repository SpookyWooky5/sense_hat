'''
@Author --> Aditya Medhe
'''
from sense_hat import SenseHat
import time

class SenseSquare(SenseHat):
    def init(self , c2):
        x1 = 0
        y1 = 0
        x2 = c2
        y2 = c2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def square(self, r,g,b):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        x2 += 1
        y2 += 1
        y_d = y2 - y1
        x_d = x2 - x1
        for i in range(x_d):
            for h in range(y_d):
                x_m = x1 + i 
                y_m = y2 + h - y_d
                self.set_pixel(x_m,y_m, r,g,b)

    def move_down(self):
        y1 = self.y1
        y2 = self.y2
        if y2 < 7:
            y1 += 1
            self.y1 = y1
            y2 += 1
            self.y2 = y2
            self.clear()
            self.square(r,g,b)
        
    def move_up(self):
        y1 = self.y1
        y2 = self.y2
        if y1 > 0:
            y1 -= 1
            self.y1 = y1
            y2 -= 1
            self.y2 = y2
            self.clear()
            self.square(r,g,b)

    def move_right(self):
        x1 = self.x1
        x2 = self.x2
        if x2 < 7:
            x1 += 1
            self.x1 = x1
            x2 += 1
            self.x2 = x2
            self.clear()
            self.square(r,g,b)

    def move_left(self):
        x1 = self.x1
        x2 = self.x2
        if x1 > 0:
            x1 -= 1
            self.x1 = x1
            x2 -= 1
            self.x2 = x2
            self.clear()
            self.square(r,g,b)

            
sense = SenseHat()
sense.clear()
sense.lowlight = False

r = 90
g = 50
b = 170           
c2 = 2
sqr = SenseSquare()
sqr.init(c2)
sqr.square(r,g,b)

rgb = {'r':(255,255,250,255,51,0,0,102,255),'g':(51,128,200,255,255,204,102,0,0),'b':(51,0,20,255,51,60,204,204,127)}

counter = 0
while True:
    time.sleep(0.4)
    #get orientation
    accl = sense.get_accelerometer_raw()
    x_a = round(accl['x'], 3)
    y_a = round(accl['y'], 3)
    #print(x_a, y_a)

    #if tilted
    if y_a > 0.25:
        try:
            sqr.move_down()
        except ValueError:
            pass       
    if y_a < -0.25:
        try:
            sqr.move_up()
        except ValueError:
            pass
    if x_a > 0.25:
        try:
            sqr.move_right()
        except ValueError:
            pass
    if x_a < -0.25:
        try:
            sqr.move_left()
        except ValueError:
            pass
    if counter > len(rgb["r"])-1 or counter < 0:
        counter = 0
    for event in sense.stick.get_events():
        if event.action == 'pressed':
#change colour
            if event.direction == "left":
                if counter != 0:
                    counter -= 1
                r = rgb["r"][counter]
                g = rgb["g"][counter]
                b = rgb["b"][counter]
                sqr.square(r,g,b)
                
            if event.direction == "right":
                if counter < len(rgb["r"])-1:
                    counter +=1
                r = rgb["r"][counter]
                g = rgb["g"][counter]
                b = rgb["b"][counter]
                sqr.square(r,g,b)
#change size
            if event.direction == "up":
                if c2 < 7:
                    c2 += 1
                    sense.clear()
                    sqr.init(c2)
                    sqr.square(r,g,b)   

            if event.direction == "down":
                if c2 > -1:
                    c2 -= 1
                    sense.clear()
                    sqr.init(c2)
                    sqr.square(r,g,b) 
