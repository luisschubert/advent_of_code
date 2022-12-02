import os

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
