import os
file_path = os.path.join('AoC_2021','day1.txt')
input = open(file_path).read().splitlines()

def is_bigger(item1, item2):
    return item1 < item2
count = sum(is_bigger(int(input[i]), int(input[i+1])) for i in range(len(input) - 1))
print('Part 1 -', count)

def hard_way(lst):
    return [sum(int(lst[i]) for i in range(j, j+3)) for j in range(len(lst) - 2)]

input2 = hard_way(input)
count1 = sum(is_bigger(input2[i], input2[i+1]) for i in range(len(input2) - 1))
print('Part 2 -', count1)