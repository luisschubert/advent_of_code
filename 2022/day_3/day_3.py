
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

def initial_solution():
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
            # print(compartment_1)
            # print(compartment_2)

            set_1 = set(compartment_1)
            set_2 = set(compartment_2)
            # print(set_1)
            # print(set_2)

            in_both_sets = ""

            for element in set_1:
                if element in set_2:
                    in_both_sets = element

            # print(in_both_sets)
            # print("\n\n")
            # pdb.set_trace()
            priority_count = priority_count + convert_character_to_priority_number(in_both_sets)

    print(priority_count)


initial_solution()
