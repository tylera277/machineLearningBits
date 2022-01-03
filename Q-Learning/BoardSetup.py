
class BoardSetup:

    def __init__(self):
        pass

    def board_layout(self):

        movableSpace = {}

        movableSpace[1] = [i for i in range(1, 12, 1)]
        movableSpace[1].remove(4)
        movableSpace[2] = [1, 3, 7, 11]
        movableSpace[3] = [1, 3, 4, 5, 6, 7, 9, 11]
        movableSpace[4] = [7, 9, 11]
        movableSpace[5] = [1, 2, 3, 4, 5, 7, 9, 11]
        movableSpace[6] = [1, 5, 7, 9]
        movableSpace[7] = [1, 2, 3, 5, 7, 9, 10, 11]
        movableSpace[8] = [3, 5, 7, 9, 11]
        movableSpace[9] = [1, 2, 3, 5, 6, 7, 9, 11]
        movableSpace[10] = [3, 9, 11]
        movableSpace[11] = [i for i in range(1, 12,1)]
        movableSpace[11].remove(10)

        return movableSpace

    def setup_ok_paths(self, rewards, movable_space, value):
        for i in range(1, 12, 1):
            for j in movable_space[i]:
                rewards[i][j] = value

        return rewards
