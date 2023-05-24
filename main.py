import random
from random import randint

num_list = [1,8,2,5,0]#[random.randint(1,100) for i in range(50)]
num_list_sorted = list()

print(num_list)

min_num = num_list[0]
index_of_min_num = 0
max_num = num_list[-1]
index_of_max_num = len(num_list) - 1
stop = len(num_list)
while len(num_list) > 0:
    for i in range(0, stop):
        if min_num > num_list[i]:
            min_num = num_list[i]
            index_of_min_num = i
            if stop - 1 == i:
                stop -= 1
                num_list_sorted.append(min_num)
                num_list.pop(index_of_min_num)
                min_num = num_list[0]
                index_of_min_num = 0
                continue
        if stop - 1 == i:
            stop -= 1
            num_list_sorted.insert(len(num_list_sorted),min_num)
            num_list.pop(index_of_min_num)
            index_of_min_num = 0



print(num_list_sorted)

    #for j in range(i + 1,stop - 1):

