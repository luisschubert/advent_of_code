

def part_1():
    containments = 0
    with open("input.txt") as file:
        for line in file:
            if line != "\n":
                assignments = line.split(",")
                a = assignments[0].split("-")
                b = assignments[1].split("-")
                if int(a[0]) < int(b[0]):
                    # b could be contained in a
                    # if b is <= a 
                    if int(a[1]) >= int(b[1]):
                        containments += 1
                    pass
                elif int(a[0]) > int(b[0]):
                    # a could be contained in a
                    # if a is <= b
                    if int(a[1]) <= int(b[1]):
                        containments += 1
                    pass
                else:
                    # they start equal
                    containments += 1

    print(containments)

def part_2():
    overlap = 0
    with open("input.txt") as file:
        for line in file:
            if line != "\n":
                assignments = line.split(",")
                a = assignments[0].split("-")
                b = assignments[1].split("-")

                # a[0] a[1], b[0] b[1]
                #  34 - 82 ,  33 - 81
                # 
                # a[0] a[1], b[0] b[1]
                #  59 - 59 ,  69 - 73

                if ( ( int(a[0]) <= int(b[1]) ) and ( int(a[1]) >= int(b[1]) ) ) or ( (int(a[1]) >= int(b[0])) and ( ( int(a[1]) <= int(b[1]) ) ) ):
                    overlap += 1

    print(overlap)


part_1()

part_2()
