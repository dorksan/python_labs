def buble_sort(array):
    j = 1
    while True:
        for i in range(len(array) - j):
            if array[i] > array[i + 1]:
                array[i] += array[i + 1]
                array[i + 1] = array[i] - array[i + 1]
                array[i] = array[i] - array[i + 1]
        j += 1
        if len(array) - j == 0:
            break
    return  array

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
array = buble_sort(array)
print(array)