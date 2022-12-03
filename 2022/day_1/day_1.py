

def quick_solution():
    res_sum = []
    intermediary = []
    with open("input.txt") as file:
        for l in file:
            if l == "\n":
                res_sum.append(sum(intermediary))
                intermediary = []
            else:
                intermediary.append(int(l.strip("\n")))

    res_sum_sorted = res_sum
    res_sum_sorted.sort(reverse=True)

    top_three = res_sum_sorted[:3]
    print(top_three)

    print("question 1 result")
    print(res_sum_sorted[0])

    print("question 2 result")
    print(sum(top_three))

# after discussing with rock the time complexity of this approach, he convinced me that
# using a heap would be better suited.
#
# my solution is currently o(n + nlog(n))
# we iterate throug the input once and build an array of values
# we then sort the list and pop off the top three items.

# another solution i had in mind was to only ever keep a list of the top three items
# as we iterate through the list we check if each new element is larger than the smallest element in our list
# if it is we replace and check the next


def improved_solution():
    res_sum = [0,0,0]
    intermediary = []
    with open("input.txt") as file:
        for l in file:
            if l == "\n":
                new_addition = sum(intermediary)
                new_index = -1
                for i, element in enumerate(res_sum):
                    if new_addition >= element:
                        new_index = i
                
                if new_index > -1:
                    res_sum.insert(new_index+1, new_addition)
                    res_sum.pop(0)
                intermediary = []
            else:
                intermediary.append(int(l.strip("\n")))

    print(res_sum)

    print("question 1 result")
    print(res_sum[2])

    print("question 2 result")
    print(sum(res_sum))


quick_solution()

improved_solution()
