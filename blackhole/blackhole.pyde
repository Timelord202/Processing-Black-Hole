# Need a class to create instance variables each time a circle is created

class DrawCircle:
    def __init__(self):
        self.size = random(10, 20)
        self.x = random(width)
        self.y = random(height)
        self.a = (width/2 - self.x)*0.01
        self.b = (height/2 - self.y)*0.01
    
    def draw_circle(self):
        self.a *= 1.1
        self.b *= 1.1
        if dist(self.x, self.y, width/2, height/2) > 200:  # Not very efficient, but I'm lazy
            return circle(self.x+self.a, self.y+self.b, self.size)

def setup():
    global x, y, a, b, stack
    
    size(1000, 1000)
    stack = []
    
def draw():
    global x, y, a, b, stack
    
    stack.append(DrawCircle())
    background(255)
    noStroke()
    for x in range(len(stack)):
        try:
            stack[x].draw_circle()
            if dist(stack[x].x + stack[x].a, 0, width/2, 0) < 20:
                stack.pop(stack.index(stack[x]))
        except IndexError:
            pass
    fill(0)
    circle(width/2, height/2, 100)
