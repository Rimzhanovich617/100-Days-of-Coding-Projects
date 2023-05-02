# Write a program that takes a list of integers as input and returns the maximum sum of any two
# adjacent numbers in the list. For example, if the input list is [1, 2, 3, 4, 5], the program
# should return 9 (which corresponds to the sum of 4 and 5).

import random

list_one = [1,2,3,4,5]


sorted_list_one = sorted(list_one)


addition = sorted_list_one[4]
addition_2 = sorted_list_one[3]
print(addition + addition_2)

import random

def max_adjacent_sum(lst):
    max_sum = float('-inf')  # initialize to negative infinity
    for i in range(len(lst)-1):
        current_sum = lst[i] + lst[i+1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Generate a random list of 10 integers between -100 and 100
lst = [random.randint(-100, 100) for i in range(10)]
print(lst)

# Find the maximum sum of any two adjacent integers in the list
max_sum = max_adjacent_sum(lst)
print("Maximum sum of adjacent integers:", max_sum)