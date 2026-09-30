import copy
import random

class Hat:
    def __init__(self, **color):
        if color:
            if sum(color.values()):
                self.contents = []
                for color, i in color.items():
                    for j in range(i):
                        self.contents.append(f'{color}')
    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        contents = copy.deepcopy(self.contents)
        balls_drawn = []
        for _ in range(num_balls_drawn):
            index = contents.index(random.choice(contents))
            balls_drawn.append(contents.pop(index))            
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

hat = Hat(red=3, blue=6, green=2)
print(hat.draw(4))