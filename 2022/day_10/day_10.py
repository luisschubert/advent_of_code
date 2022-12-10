
le_significant_steps = [20,60,100,140,180,220]

le_values = []

def check(cycle_count, x):
    print("cycle_count:{} x:{}".format(cycle_count,x))
    if cycle_count in le_significant_steps:
        le_values.append(x*cycle_count)

    

with open("input.txt") as file:
    x = 1
    cycle_count = 0
    for line in file:
        if line != "/n":
            input = line.strip("\n").split(" ")
            print(input)
            instruction = input[0]
            if instruction == "noop":
                print("noop")
                cycle_count += 1
                check(cycle_count, x)
            
            if instruction == "addx":
                cycle_count += 1
                check(cycle_count, x)
                cycle_count += 1
                check(cycle_count, x)
                x = x + (int(input[1]))
                
    
    for i, p in enumerate(le_values):
        print("i:{} v:{} s:{}".format(i, p , le_significant_steps[i]))

    print(sum(le_values))
