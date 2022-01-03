
import numpy as np


class UpdateQValues:

    def __init__(self, q_array, reward_array, current_position,
                 next_position, action_direction, max_q_actionDirection_nextPos,
                 learning_rate, discount_factor):

        self.q_array = q_array
        self.reward_array = reward_array
        self.yCurrPos = current_position[0]
        self.xCurrPos = current_position[1]
        self.yNextPos = next_position[0]
        self.xNextPos = next_position[1]
        self.action_direction = str(action_direction)
        self.max_q_actionDirection_nextPos = str(max_q_actionDirection_nextPos)
        self.lr = learning_rate
        self.df = discount_factor

    def direction_2_number(self, direction):
        if direction == 'left':
            direction_number = 0
        elif direction == 'up':
            direction_number = 1
        elif direction == 'right':
            direction_number = 2
        elif direction == 'down':
            direction_number = 3
        else:
            raise ValueError('Not a valid direction entered.')

        return direction_number


    def update_q_values(self):

        action_direction_number = self.direction_2_number(self.action_direction)
        max_q_nextPos_number = self.direction_2_number(self.max_q_actionDirection_nextPos)

        inside_product = self.reward_array[self.yNextPos][self.xNextPos] + self.df*max_q_nextPos_number - \
                         self.q_array[self.yCurrPos][self.xCurrPos][action_direction_number]

        self.q_array[self.yCurrPos][self.xCurrPos][action_direction_number] += self.lr * inside_product

        return self.q_array


