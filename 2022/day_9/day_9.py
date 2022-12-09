
Y = 1
X = 0

def update_position_for_rope(rope, knot_id):
    if (abs(rope[knot_id-1][X] - rope[knot_id][X]) == 2):
        # tail needs to move in the x direction
        if rope[knot_id-1][X] > rope[knot_id][X]:
            rope[knot_id][X] += 1
        elif rope[knot_id-1][X] < rope[knot_id][X]:
            rope[knot_id][X] -= 1
        else:
            assert True == False

        if rope[knot_id-1][Y] != rope[knot_id][Y]:
            if rope[knot_id-1][Y] > rope[knot_id][Y]:
                rope[knot_id][Y] += 1
            elif rope[knot_id-1][Y] < rope[knot_id][Y]:
                rope[knot_id][Y] -= 1
            else:
                assert True == False
            
    elif (abs(rope[knot_id-1][Y] - rope[knot_id][Y]) == 2):
        if rope[knot_id-1][Y] > rope[knot_id][Y]:
            rope[knot_id][Y] += 1
        elif rope[knot_id-1][Y] < rope[knot_id][Y]:
            rope[knot_id][Y] -= 1
        else:
            assert True == False

        if rope[knot_id-1][X] != rope[knot_id][X]:
            if rope[knot_id-1][X] > rope[knot_id][X]:
                rope[knot_id][X] += 1
            elif rope[knot_id-1][X] < rope[knot_id][X]:
                rope[knot_id][X] -= 1
            else:
                assert True == False



def run_solution():
    rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    tail_positions = set([])

    with open("input.txt") as file:
        for line in file:
            if line != "\n":
                postions = line.split(" ")
                direction = postions[0]
                magnitude = int(postions[1])

                for i in range(magnitude):
                    if "U" == direction:
                        # positive y direction
                        rope[0][Y] += 1
                        pass
                    elif "D" == direction:
                        # negative y direction
                        rope[0][Y] -= 1
                        pass
                    elif "L" == direction:
                        # negative x direction
                        # head_x -=1
                        pass
                    elif "R" == direction:
                        # positive x direction
                        rope[0][X] += 1
                        pass
                    else:
                        assert True == False


                    for i in range(1, len(rope)):
                        update_position_for_rope(rope, i)
                    
                    current_position = "{}_{}".format(str(rope[len(rope)-1][X]), str(rope[len(rope)-1][Y]))
                    tail_positions.add(current_position)

                

        print("num_positions: {}".format(len(tail_positions)))
                





run_solution()
