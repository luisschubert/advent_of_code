def run_solution():
    head_x = 0
    head_y = 0

    tail_x = 0
    tail_y = 0

    tail_positions = set([])

    with open("input.txt") as file:
        for line in file:
            if line != "\n":
                postions = line.split(" ")
                direction = postions[0]
                magnitude = int(postions[1])

                print(line)
                for i in range(magnitude):
                    if "U" == direction:
                        # positive y direction
                        head_y += 1
                        pass
                    elif "D" == direction:
                        # negative y direction
                        head_y -=1
                        pass
                    elif "L" == direction:
                        # negative x direction
                        head_x -=1
                        pass
                    elif "R" == direction:
                        # positive x direction
                        head_x += 1
                        pass
                    else:
                        assert True == False
                    
                    
                    if (abs(head_x - tail_x) == 2):
                        # tail needs to move in the x direction
                        if head_x > tail_x:
                            tail_x += 1
                        elif head_x < tail_x:
                            tail_x -= 1
                        else:
                            assert True == False

                        if head_y != tail_y:
                            if head_y > tail_y:
                                tail_y += 1
                            elif head_y < tail_y:
                                tail_y -= 1
                            else:
                                assert True == False
                            
                    elif (abs(head_y - tail_y) == 2):
                        if head_y > tail_y:
                            tail_y += 1
                        elif head_y < tail_y:
                            tail_y -= 1
                        else:
                            assert True == False

                        if head_x != tail_x:
                            if head_x > tail_x:
                                tail_x += 1
                            elif head_x < tail_x:
                                tail_x -= 1
                            else:
                                assert True == False


                    print("head x:{} y:{}".format(head_x, head_y))
                    print("tail x:{} y:{}".format(tail_x, tail_y))
                    print("\n")
                    #encode y position
                    current_position = "{}_{}".format(str(tail_x), str(tail_y))
                    tail_positions.add(current_position)
                print("\n\n\n")

                

        print("num_positions: {}".format(len(tail_positions)))
                





run_solution()
