#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for a in range(list_length):
        try:
            div = my_list_1[a] / my_list_2[a]
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return (result)
