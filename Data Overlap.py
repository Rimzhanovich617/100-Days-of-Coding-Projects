import os

def frequency():
    f = open('file1.txt', "r")
    l = []

    for line in f:
        line = line.strip('\n')
        start = line.find("[")
        end = line.find("]")
        line = line[start + 1:end]
        l.extend([int(i) for i in line.split(',')])
        print(line)

    print(l)

frequency()
def is_empty_1(file_name):
    return os.path.isfile(file_name) and os.path.getsize(file_name) == 0
file_path = "file1.txt"
is_empty = is_empty_1("file1.txt")

def is_empty_2(file_name):
    return os.path.isfile(file_name) and os.path.getsize(file_name) == 0
file_path2 = "file2.txt"
is_empty2 = is_empty_2("file2.txt")

f = open("file1.txt", "r")
lines = f.readlines()
list1 = []
new_list1 = list1.append(lines)
print(new_list1)


f1 = open("file2.txt", "r")
lines1 = f.readlines()
print("Total nuber of integers: ", len(lines))




