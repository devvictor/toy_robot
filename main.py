import sys

INCREMENTS = {"NORTH": (0, 1),  "WEST": (-1, 0),
              "SOUTH": (0, -1), "EAST": (1, 0)}

DIRECTIONS = list(INCREMENTS.keys())

def main(filename):

    """
    Main logic to control the robot's initial placement, movement, turning and reporting. 
    Please refer to PROBLEM.md for detailed requirement. 

    Parameters: filename - pass a txt file to the program
    Returns: string - final postion coordinate of the robot with the facing direction.
    """ 
    
    # loop through the input file
    with open(filename) as fp:
        lines = fp.readlines()

    position = None

    for line in lines:

        # finding a valid PLACE command
        if line.startswith("PLACE "):

            l = line.strip().split()
            loc = l[1]

            sl = loc.split(",")

            x = sl[0]
            y = sl[1]
            f = sl[2]

            x = int(x)
            y = int(y)
            
            if 0 <= x < 5 and 0 <= y < 5:
                position = (x, y)
                continue
            else:
                print('Robot is not on the table.')

        # if not placed yet, skip to next line
        if position is None:
            continue
            
        # if placed, proceed
        command = line.strip()

        # LEFT command 
        if command == "LEFT":

            index_f = DIRECTIONS.index(f)
            f = DIRECTIONS[(index_f+1) % 4]

        # RIGHT command 
        elif command == "RIGHT":

            index_f = DIRECTIONS.index(f)
            f = DIRECTIONS[(index_f-1) % 4]

        # MOVE command
        elif command == "MOVE":

            inc = INCREMENTS[f]

            u = position[0] + inc[0]
            v = position[1] + inc[1]

            if 0 <= u < 5 and 0 <= v < 5:
                position = (u, v)

        # REPORT the final coordinates and facing direction
        elif command == "REPORT":

            x, y = position
            print(f"{x},{y},{f}")

if __name__ == "__main__":
    main(sys.argv[1])