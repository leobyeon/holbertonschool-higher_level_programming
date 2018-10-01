#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list[:x]:
        try:
            print(i, end='')
            count += 1
        except SyntaxError:
            print("x is greater than the length of the list.")
    print()
    return count
