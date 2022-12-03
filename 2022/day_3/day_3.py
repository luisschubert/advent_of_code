
import pdb

def convert_character_to_priority_number(character):
    integer_rep = ord(character)
    priority_num = 0
    if (integer_rep >= 97) and (integer_rep <= (97+25)):
        priority_num = integer_rep - 96
    elif (integer_rep >= 65) and (integer_rep <= (65+25)):
        priority_num = integer_rep - 64 + 26
    else:
        assert False is True
    return priority_num

def part_1_solution():
    priority_count = 0
    with open("input.txt") as file:
        for line in file:
            # remove \n
            sanitized_items = line.strip()
            # get item count
            items_in_backpack = len(sanitized_items)

            # ignore last line with newline
            if items_in_backpack == 0:
                continue

            # assumption is that count of items is even
            assert (items_in_backpack & 1) == 0 

            midpoint = int(items_in_backpack/2)

            compartment_1 = sanitized_items[:midpoint]
            compartment_2 = sanitized_items[midpoint:]

            set_1 = set(compartment_1)
            set_2 = set(compartment_2)

            in_both_sets = ""

            for element in set_1:
                if element in set_2:
                    in_both_sets = element

            priority_count = priority_count + convert_character_to_priority_number(in_both_sets)

    print(priority_count)

def part_2_solution():

    def get_badge(group):
        set_1 = group[0]
        set_2 = group[1]
        set_3 = group[2]
        
        in_all_sets = None

        for element in set_1:
            if (element in set_2) and (element in set_3):
                in_all_sets = element
        return in_all_sets

    priority_count = 0
    count = 0
    new_group = []
    with open("input.txt") as file:
        for line in file:
            # remove \n
            sanitized_items = line.strip()

            new_group.append(sanitized_items)
            count = count + 1
            if count == 3:
                priority_count = priority_count + convert_character_to_priority_number(get_badge(new_group))
                new_group = []
                count = 0

    print(priority_count)

part_1_solution()
part_2_solution()
