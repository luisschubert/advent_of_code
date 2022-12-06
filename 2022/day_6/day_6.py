
def run_solution(marker_size=4):
    with open("input.txt") as file:
        line = file.readline()

        for i in range(len(line)-marker_size):
            if len(set(line[i:i+marker_size])) == marker_size:
                print(i+marker_size)
                break

def part_1():
    run_solution()

def part_2():
    run_solution(14)

part_1()

part_2()
