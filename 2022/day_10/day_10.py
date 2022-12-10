
def part_1():
    le_significant_steps = [20,60,100,140,180,220]

    le_values = []

    def check(cycle_count, x):
        # print("cycle_count:{} x:{}".format(cycle_count,x))
        if cycle_count in le_significant_steps:
            le_values.append(x*cycle_count)


    with open("input.txt") as file:
        x = 1
        cycle_count = 0
        for line in file:
            if line != "/n":
                input = line.strip("\n").split(" ")
                instruction = input[0]
                if instruction == "noop":
                    cycle_count += 1
                    check(cycle_count, x)
                
                if instruction == "addx":
                    cycle_count += 1
                    check(cycle_count, x)
                    cycle_count += 1
                    check(cycle_count, x)
                    x = x + (int(input[1]))
                    
        
        # for i, p in enumerate(le_values):
        #     print("i:{} v:{} s:{}".format(i, p , le_significant_steps[i]))

        print(sum(le_values))


def part_2():
    image = ["","","","","",""]

    def check(cycle_count, x):
        i = (cycle_count-1) // 40
        k = (cycle_count-1) - (40 * i)
        # print ("i:{} k:{} c:{} x:{}".format(i,k,cycle_count,x))
        value = ""
        if k in [x-1, x, x+1]:
            value = "X"
        else:
            value = "."
        image[i] = image[i] + value


    with open("input.txt") as file:
        x = 1
        cycle_count = 0
        for line in file:
            if line != "/n":
                input = line.strip("\n").split(" ")
                instruction = input[0]
                if instruction == "noop":
                    cycle_count += 1
                    check(cycle_count, x)
                
                if instruction == "addx":
                    cycle_count += 1
                    check(cycle_count, x)
                    cycle_count += 1
                    check(cycle_count, x)
                    x = x + (int(input[1]))
                    
    for i in image:
        print(i)


part_1()

part_2()
