# Write a program that takes a list of integers as input and returns a new list containing only
# the even numbers from the input list. For example, if the input
# list is [1, 2, 3, 4, 5, 6, 7, 8, 9], the program should return [2, 4, 6, 8].
# Note that the input list can be of any length and may contain both even and odd numbers.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, list1)
print(list(result))