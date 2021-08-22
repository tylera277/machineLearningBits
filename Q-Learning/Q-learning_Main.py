# 8/19/2021
# Q-L reinforcement learning attempt

import numpy as np

board_rows = 13
board_columns = 13

q_values = np.zeros((board_rows, board_columns, 4))

actions = ['up', 'right', 'down', 'left']

rewards = np.full((board_rows, board_columns), -100)

# mapping the movable space between rows and columns 1 & 11
movableSpace = {}

movableSpace[1] = [i for i in range(1, 12)]
movableSpace[1].remove(4)
movableSpace[2] = [1, 3, 7, 11]
movableSpace[3] = [1, 3, 4, 5, 6, 7, 9, 11]
movableSpace[4] = [7, 9, 11]
movableSpace[5] = [1, 2, 3, 4, 5, 7, 9, 11, 12]
movableSpace[6] = [1, 5, 7, 9]
movableSpace[7] = [1, 2, 3, 5, 7, 9, 10, 11]
movableSpace[8] = [3, 5, 7, 9, 11]
movableSpace[9] = [0, 1, 2, 3, 5, 6, 7, 9, 11]
movableSpace[10] = [3, 9, 11]
movableSpace[11] = [i for i in range(1, 12)]
movableSpace[11].remove(10)

# set the rewards at the movable spaces to -1
for row_index in range(1,12):
    for column_index in movableSpace[row_index]:
        rewards[row_index, column_index] = -1

rewards[5, 12] = 100
#for row in rewards:
#    print(row)
#rewards[3,0] = 100
# +this function determines whether the specified location is a
# terminal state
def is_terminal_state(current_row_index, current_column_index):
    if rewards[current_row_index, current_column_index] == -1:
        return False
    else:
        return True

# +define an epsilon greedy algorithm that will choose which action
# to take next
def get_next_action(current_row_index, current_column_index, epsilon):
    # +if a randomly chosen value between zero and 1 is less than
    # epsilon, then choose the most promising value from the Q-table
    # for this state

    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_column_index])

    else:
        return np.random.randint(4)

def get_starting_location():
    current_row_index = np.random.randint(board_rows)
    current_column_index = np.random.randint(board_columns)
    while is_terminal_state(current_row_index, current_column_index):
        current_row_index = np.random.randint(board_rows)
        current_column_index = np.random.randint(board_columns)
    return current_row_index, current_column_index



#define a function that will get the next location based on the chosen action
def get_next_location(current_row_index, current_column_index, action_index):
  new_row_index = current_row_index
  new_column_index = current_column_index
  if actions[action_index] == 'up' and current_row_index > 0:
    new_row_index -= 1
  elif actions[action_index] == 'right' and current_column_index < board_columns - 1:
    new_column_index += 1
  elif actions[action_index] == 'down' and current_row_index < board_rows - 1:
    new_row_index += 1
  elif actions[action_index] == 'left' and current_column_index > 0:
    new_column_index -= 1
  return new_row_index, new_column_index

# Define a function that will get the shortest path between any location within the warehouse that
# the robot is allowed to travel and the item packaging location.
def get_shortest_path(start_row_index, start_column_index):
    if is_terminal_state(start_row_index, start_column_index):
        return []
    else:
        current_row_index, current_column_index = start_row_index, start_column_index
        shortest_path = []
        shortest_path.append([current_row_index, current_column_index])
        while not is_terminal_state(current_row_index, current_column_index):
            # get the best action to take
            action_index = get_next_action(current_row_index, current_column_index, epsilon)
            current_row_index, current_column_index = get_next_location(current_row_index,
                                                                        current_column_index,
                                                                        action_index)
            shortest_path.append([current_row_index, current_column_index])
    return shortest_path


################ ################### ################# ###############

# define training parameters
epsilon = 0.9

discount_factor = 0.9
learning_factor = 0.9
for episode in range(1000):
    row_index, column_index = get_starting_location()
    while not is_terminal_state(row_index, column_index):
        action_index = get_next_action(row_index, column_index, epsilon)
        old_row_index, old_column_index = row_index, column_index
        row_index, column_index = get_next_location(row_index, column_index,\
                                                   action_index)
        reward = rewards[row_index, column_index]
        old_q_value = q_values[old_row_index, old_column_index, action_index]

        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, column_index])) - old_q_value

        new_q_value = old_q_value + (learning_factor * temporal_difference)

        q_values[old_row_index, old_column_index, action_index] = new_q_value

print(get_shortest_path(9, 0))