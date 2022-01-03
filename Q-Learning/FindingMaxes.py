
import numpy as np

class FindMaxes:

    def __init__(self):
        pass

    def find_max_q(self, position, qArray):
        y_pos = position[0]
        x_pos = position[1]

        up = qArray[y_pos-1][x_pos][1]
        down = qArray[y_pos+1][x_pos][3]
        left = qArray[y_pos][x_pos-1][0]
        right = qArray[y_pos][x_pos+1][2]

        values = [up, down, left, right]
        if up == max(values):
            return 'up'
        elif down == max(values):
            return 'down'
        elif left == max(values):
            return 'left'
        elif right == max(values):
            return 'right'
        else:
            raise ValueError("No max found!")
