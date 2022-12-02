import os


res = []
res_sum = []
intermediary = []
with open("input.txt") as file:
    for l in file:
        if l == "\n":
            res.append(intermediary)
            res_sum.append(sum(intermediary))
            intermediary = []
        else:
            intermediary.append(int(l.strip("\n")))

for i in res:
    print(i)


print(max(res_sum))
