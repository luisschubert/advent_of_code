
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
