# Write a program that takes a string as input and returns a new string that contains only the
# unique alphanumeric characters from the input string.
# For example, if the input string is "hello world!",
# the program should return "helowrd".

# Note that the output string should preserve the order of the unique characters from the input
# string. Additionally, the input string may contain spaces and/or special characters, and the
# output string should only contain alphanumeric characters.

string = "hello world"
unique_chars = []
for char in string:
    if not char.isalnum():
        continue
    if string.count(char) >= 2 :
        unique_chars.append(char)
print(''.join(unique_chars))

