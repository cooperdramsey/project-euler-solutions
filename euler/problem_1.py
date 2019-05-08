# Problem 1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np


def sum_of_multiples(value):
    value_list = np.arange(1, value)
    value_list_3 = np.mod(value_list, 3)
    value_list_5 = np.mod(value_list, 5)
    result_3 = np.add(np.where(value_list_3 == 0), 1)
    result_5 = np.add(np.where(value_list_5 == 0), 1)
    result = np.concatenate((result_3, result_5), axis=1)
    return np.sum(np.unique(result))


if __name__ == '__main__':
    value = 1000
    print(sum_of_multiples(value))
