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
            balls_drawn = copy.deepcopy(self.contents)
            self.contents.clear()
            self.contents = []
            return balls_drawn
        balls_drawn = []
        for _ in range(num_balls_drawn):
            index = self.contents.index(random.choice(self.contents))
            balls_drawn.append(self.contents.pop(index))     
            print(self.contents)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    for key, value in expected_balls.items():
        for _ in range(value):
            expected.append(key)
    N = num_experiments
    M = 0
    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        balls_drawn = copied_hat.draw(num_balls_drawn)
        are_in = True
        for ball in expected:
            if ball in balls_drawn:
                balls_drawn.pop(balls_drawn.index(ball))
            else:
                are_in = False
                break
        if are_in:
            M += 1
    return M/N