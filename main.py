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

def binary_search(number, sorted_list):
    result_ok = False
    first = 0
    last = len(sorted_list) - 1
    print(last)
    while first < last:
        middle = (first + last) // 2
        if number == sorted_list[middle]:
            first = middle
            last = first
            result_ok = True
            position = middle
        else:
            if number > sorted_list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if result_ok:
        print(f"Element was found on position {position}")
    else:
        print("Element was not found")

sorted_list = selection_sort(num_list)
print(sorted_list)
binary_search(15, sorted_list)

