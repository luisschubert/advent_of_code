
def run_solution(part_1=True):
    le_map = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    count = 0
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                break
            else:
                # 9 entries
                # 9 entries of 3 characters plus 8 spaces
                if count < 8:
                    if line[1] != " ":
                        le_map[0].append(line[1])
                    l = line[4:]
                    for i in range(0,8):
                        if l[1] != " ":
                            le_map[i+1].append(l[1])
                        if i != 8:
                            l = l[4:]

                    count += 1

        print(le_map)
        
        for line in file:
            if line != "\n":
                l = line.split(" ")
                move_count = int(l[1])
                src = int(l[3])
                dest = int(l[5])

                # print(line)
                for i in range(move_count):
                    # print("src")
                    # print(le_map[src-1])
                    # print("dest")
                    # print(le_map[dest-1])

                    # print('i: {} and count: {} will attempt to pop({})'.format(i,move_count, ((move_count - 1) - i)))
                    if part_1:
                        le_map[dest-1].insert(0,le_map[src-1].pop(0))
                    else:
                        le_map[dest-1].insert(0, le_map[src-1].pop((move_count - 1) - i))
                
                # print("src")
                # print(le_map[src-1])
                # print("dest")
                # print(le_map[dest-1])
                # print("####\n\n\n")





        # print(le_map)

    result = ""
    for i in le_map:
        result += i.pop(0)

    print(result)


#part_1:
run_solution()

#part_2
run_solution(False)
