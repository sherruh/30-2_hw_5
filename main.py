from random import randint

num_list = [randint(1,100) for i in range(50)]

print(num_list)

def selection_sort(num_list):
    num_list_sorted = list()
    while len(num_list) > 0:
        min_num = num_list[0]
        for i in range(0,len(num_list)):
            if min_num > num_list[i]:
                min_num = num_list[i]
        num_list_sorted.append(min_num)
        num_list.pop(num_list.index(min_num))
    return num_list_sorted

print(selection_sort(num_list))

