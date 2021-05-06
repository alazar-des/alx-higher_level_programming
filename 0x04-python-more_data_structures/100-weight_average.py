#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return sum(x[0] * x[1] for x in my_list) / sum(x[1] for x in my_list)
