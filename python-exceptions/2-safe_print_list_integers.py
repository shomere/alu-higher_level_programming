#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")  # Try to print as an integer
            count += 1  # Increment count only if it's an integer
        except (ValueError, TypeError):
            # Skip non-integer values silently
            continue
        except IndexError:
            # Stop if x exceeds the length of my_list
            break
    print()  # Newline after printing all integers
    return count


