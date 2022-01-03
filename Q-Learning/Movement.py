import numpy as np

class Movement:

    def __init__(self, position, direction):
        self.yPos = position[0]
        self.xPos = position[1]
        self.direction = str(direction)


    def Move(self):
        if self.direction == 'up':
            self.yPos -= 1
        if self.direction == 'down':
            self.yPos += 1
        if self.direction == 'left':
            self.xPos -= 1
        if self.direction == 'right':
            self.xPos += 1

        return np.array([self.yPos, self.xPos])

    def Moverino(self, x_pos, y_pos, direction):
        xPos = x_pos
        yPos = y_pos
        if direction == 'up':
            yPos -= 1
        if direction == 'down':
            yPos += 1
        if direction == 'left':
            xPos -= 1
        if direction == 'right':
            xPos += 1

        positionerino = yPos, xPos
        return positionerino

    def determine_longest_path(self, q_values, starting_point, end_point):
        position = starting_point
        movement_list = []

        prev_move = 2
        for i in range(1, 50):
            y_pos = position[0]
            x_pos = position[1]



            if prev_move == 0:
                q_values[y_pos][x_pos][2] = -100
            elif prev_move == 2:
                q_values[y_pos][x_pos][0] = -100
            if prev_move == 1:
                q_values[y_pos][x_pos][3] = -100
            elif prev_move == 3:
                q_values[y_pos][x_pos][1] = -100


            move = np.argmax(q_values[y_pos][x_pos])

            if move == 0:
                direction = 'left'
            elif move == 1:
                direction = 'up'
            elif move == 2:
                direction = 'right'
            else:
                direction = 'down'

            position = Movement(position, direction).Moverino(x_pos, y_pos, direction)
            movement_list.append(position)
            if (y_pos == end_point[0]) and (x_pos == end_point[1]):
                print("le fin")
                return movement_list

            prev_move = move

        return movement_list

