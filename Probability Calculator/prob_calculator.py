import copy
import random
# Consider using the modules imported above.

class Hat:

    # constructor
    def __init__(self, **no_of_balls):
        # add balls to contents
        self.contents = []
        for k, v in no_of_balls.items():
            for i in range(v):
                self.contents.append(k)


    def draw(self, draw_balls):
        
        balls = []
        for i in range(draw_balls):
            
            if len(self.contents) == 0:
                break

            idx = random.randint(0, len(self.contents) - 1)
            balls.append(self.contents[idx])
            self.contents.pop(idx)
    
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    M = 0
    N = num_experiments
  
    for i in range(N):
        
        new_hat = copy.deepcopy(hat)

        balls_drawn = new_hat.draw(num_balls_drawn)
        balls_drawn_dict = get_counts(balls_drawn)
        
        state = True
        for ball, count in expected_balls.items():
            if not(ball in balls_drawn_dict) or count > balls_drawn_dict[ball]:
                state = False
                break
        
        # if experiement correct
        if state is True:
            M += 1

    return M / N

def get_counts(balls):
    ans = {}
    for ballA in balls:
        count = 0
        for ballB in balls:
            if ballA == ballB:
                count += 1
        ans[ballA] = count
    return ans