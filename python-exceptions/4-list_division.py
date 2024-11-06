#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            # Attempt to divide elements at index `i` of both lists
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            # If an index is out of range, append 0 and print an error
            print("out of range")
            result = 0
        except TypeError:
            # If the types aren't compatible for division, append 0 and print an error
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # If there's a division by zero, append 0 and print an error
            print("division by 0")
            result = 0
        finally:
            # Append the result (either division result or 0)
            result_list.append(result)
    return result_list
 
