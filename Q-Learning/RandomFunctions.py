
def check_legality(next_pos, rows):
    yPos = next_pos[0]
    xPos = next_pos[1]
    if (xPos < 0) or (yPos < 0):
        return 0
    if (xPos >= (rows-1)) or (yPos >= (rows-1)):
        return 0

