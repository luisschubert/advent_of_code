
TYPE_DIR = 1
TYPE_FILE = 2

class fs_node():
    def __init__(self, name, type=TYPE_DIR, size=-1):
        self.name = name
        self.type = type
        self.size = int(size)
        self.sub_nodes = []
    
    def get_size(self):
        if self.size == -1:
            self.size = 0 
            if self.type == TYPE_DIR:
                for i in self.sub_nodes:
                    if i.type == TYPE_FILE:
                        self.size += i.size
                    elif i.type == TYPE_DIR:
                        self.size += i.get_size()
                    else:
                        pass
        return self.size


def print_file_tree(root_dir, depth):
    d = ""
    for i in range(depth):
        d += "\t"
    if root_dir.type == TYPE_DIR:
        print("{}{}".format(d,root_dir.name))
        for i in root_dir.sub_nodes:
            print_file_tree(i, depth+1)
    elif root_dir.type == TYPE_FILE:
        print("{}{}".format(d,root_dir.name))
    else:
        pass

def parse_file_tree(parent_node, current_node, file_reader):
    # always expect an ls or a cd ..
    s = file_reader.readline()
    s = file_reader.readline().split()

    # first get all contents
    while (s[0] != "$"):
        if s[0] == "dir":
            current_node.sub_nodes.append(fs_node(s[1]))
        else:
            current_node.sub_nodes.append(fs_node(s[1], TYPE_FILE, s[0]))
        s = file_reader.readline().split()
        if len(s) == 0:
            return

    # now go into all sub dirs
    while (".." not in s):
        id = -1
        new_dir = s[2]
        for i,p in enumerate(current_node.sub_nodes):
            if p.name == new_dir:
                id = i
        assert id != -1
        parse_file_tree(current_node, current_node.sub_nodes[id], file_reader)
        s = file_reader.readline().split()
        if len(s) == 0:
            return
    return



def run_solution():
    with open("input.txt") as file:
        s = file.readline()
        if "$ cd" in s:
            s_spl = s.split()
            root_node = fs_node(s_spl[2])
            parse_file_tree(None, root_node, file)

            # print_file_tree(root_node, 0)

            space_used = root_node.get_size()
            total_space         = 70000000
            needed_for_update   = 30000000
            needed_to_delete = needed_for_update - (total_space - space_used)
            print("space_used: {}".format(space_used))
            print("total_space: {}".format(total_space))
            print("needed_for_update: {}".format(needed_for_update))
            print("needed_to_delete: {}".format(needed_to_delete))

            min = get_smallest_directory_greater_than(root_node, needed_to_delete, total_space)

            print("min: {}".format(min))


            total = check_subdirs_for_dir_size_less_than(root_node, 100000)
            print(total)


def check_subdirs_for_dir_size_less_than(node, max_size):
    t = 0
    if (node.type == TYPE_DIR):
        if node.size < max_size:
            t =+ node.size
        for i in node.sub_nodes:
            t += check_subdirs_for_dir_size_less_than(i, max_size)
    return t


def get_smallest_directory_greater_than(node, min, max):
    ret = -1
    if (node.type == TYPE_DIR):
        if node.size >= min and node.size < max:
            ret = node.size
        new_max = max
        if ret > 0 and ret < max:
            new_max = ret
        for i in node.sub_nodes:
            sub_r = get_smallest_directory_greater_than(i, min, new_max)
            if sub_r > 0 and sub_r < new_max:
                new_max = sub_r
                ret = sub_r
    
    return ret

    

run_solution()
