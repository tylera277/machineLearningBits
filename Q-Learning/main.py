import random

import numpy as np

from BoardSetup import BoardSetup
from Movement import Movement
from FindingMaxes import FindMaxes
from UpdateQValues import UpdateQValues
from RandomFunctions import check_legality

board_rows, board_columns = 14, 14

rewards = np.full((board_rows, board_columns), -100)
q_values = np.zeros((board_rows, board_columns, 4))

# Hyper parameters
epsilon = 0.8
learningRate = 0.8
discountFactor = 0.8

moves = ['left', 'up', 'right', 'down']


board = BoardSetup()

# Function which houses the layout of the puzzle
# I want to solve
movableSpace = board.board_layout()

# Sets the boundaries to a particular value in the reward array
rewards = board.setup_ok_paths(rewards, movableSpace, -1)

# Finish grid point
rewards[5][12] = 100

# Loop parameters
t = 0
tEnd = 30
numb_of_episodes = 1000

start_position = [9, 1]
end_position = [5, 12]

for episode in range(1, numb_of_episodes, 1):

    currentPosition = [9, 1]
    nextPosition = currentPosition
    t = 0

    while t < tEnd:

        # Greedy Algorithm Selection
        if random.uniform(0, 1) < epsilon:
            direction = random.choice(moves)
            nextPosition = Movement(currentPosition, direction).Move()
            checker = check_legality(nextPosition, board_rows)
            if checker == 0:
                break

            # explore (random movement)
        else:
            direction = FindMaxes().find_max_q(currentPosition, q_values)
            nextPosition = Movement(currentPosition, direction).Move()
            checker = check_legality(nextPosition, board_rows)
            if checker == 0:
                break
            # exploit (max Q value at curr. pos)


        max_q_action_direction_nextPos = FindMaxes().find_max_q(nextPosition, q_values)

        q_values = UpdateQValues(q_array=q_values,
                                 reward_array=rewards,
                                 current_position=currentPosition,
                                 next_position=nextPosition,
                                 action_direction=direction,
                                 max_q_actionDirection_nextPos=max_q_action_direction_nextPos,
                                 learning_rate=learningRate,
                                 discount_factor=discountFactor
                                 ).update_q_values()
        currentPosition = nextPosition

        t += 1

    if episode >= ((1.0*numb_of_episodes)/2.0):
        learningRate = 0.5

print(q_values[9][1])
# Determine if a path leads from the start to the finish
path = Movement(currentPosition, direction).determine_longest_path(q_values,
                                                                   start_position,
                                                                   end_position)

print(path)

#print(q_values[5][1])

