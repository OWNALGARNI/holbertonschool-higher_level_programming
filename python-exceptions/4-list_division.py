#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
            elif b == 0:
                print("division by 0")
            else:
                result = a / b

        except IndexError:
            print("out of range")

        finally:
            new_list.append(result)

    return new_list
