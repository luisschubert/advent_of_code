def check_if_tree_visible(a, r, c, num_rows, num_columns):
    compare = a[r][c]
    # check left
    left_visible = True
    for i in range(c):
        if a[r][i] >= compare:
            left_visible = False
            
    # check right
    right_visible = True
    for i in range(c+1,num_columns):
        if a[r][i] >= compare:
            right_visible = False
    
    # check top
    top_visible = True
    for i in range(r):
        if a[i][c] >= compare:
            top_visible = False

    # check bottom
    bottom_visible = True
    for i in range(r+1,num_rows):
        if a[i][c] >= compare:
            bottom_visible = False

    return left_visible or right_visible or top_visible or bottom_visible


def get_max_scenic_score(a, r, c, num_rows, num_columns):

    compare = a[r][c]

    # viewing distance left
    vd_left = c 
    for i in range(c-1, -1, -1):
        if a[r][i] >= compare:
            vd_left = c - i
            break

    # viewing distance right
    vd_right = (num_columns-1) - c  
    for i in range(c+1, num_columns):
        if a[r][i] >= compare:
            vd_right = i - c
            break

    # viewing distance top
    vd_top = r 
    for i in range(r-1, -1, -1):
        if a[i][c] >= compare:
            vd_top = r - i
            break
    
    # viewing distance bottom
    vd_bottom = (num_rows-1) - r  
    for i in range(r+1, num_rows):
        if a[i][c] >= compare:
            vd_bottom = i - r
            break

    total_vd =vd_left * vd_right * vd_top * vd_bottom
    
    # print("compare:{} at [{}][{}]".format(compare,r,c))
    # print("vd_left: {}".format(vd_left))
    # print("vd_right: {}".format(vd_right))
    # print("vd_top: {}".format(vd_top))
    # print("vd_bottom: {}".format(vd_bottom))
    # print("total_vd: {}".format(total_vd))
    # print("\n\n\n")


    return total_vd





def run_solution():
    a = []
    # parse the data into a two dimensional array
    with open("input.txt") as file:
        for line in file:
            if line != "\n":
                b = line.strip("\n")
                a.append([int(x) for x in b])
    num_rows = len(a)
    num_columns = len(a[0])
    print("rows: {}".format(num_rows))
    print("columns: {}".format(num_columns))
    total = 0
    max_scenic_score = 0
    for r in range(1,num_rows-1):
        for c in range(1,num_columns-1):
            if check_if_tree_visible(a, r, c, num_rows, num_columns):
                total += 1
            current_scenic_score = get_max_scenic_score(a, r, c, num_rows, num_columns)
            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score
    
    # forgot about the outside trees
    outside = num_columns + (num_rows-1) + (num_rows - 1) + (num_columns - 2)

    total = total + outside

    print("num of visible trees: {}".format(total))
    print("max_scenic_score: {}".format(max_scenic_score))

run_solution()
