def qsort(array, start, end):
    if end - start <= 1:
        return
    key = array[int((start + end) // 2)]
    counterStart = start
    counterEnd = end
    while counterStart <= counterEnd:
        if array[counterStart] >= key:
            while array[counterEnd] > key:
                counterEnd -= 1
            if counterStart >= counterEnd:
                break
            tmp = array[counterStart]
            array[counterStart] = array[counterEnd]
            array[counterEnd] = tmp
        counterStart += 1
    qsort(array, start, counterStart - 1)
    qsort(array, counterStart, end)

def combSort(array):
    step = len(array) - 1
    while step >= 1:
        for i in range(len(array)):
            if (i + step) > (len(array) - 1):
                break
            if array[i] > array[i+step]:
                tmp = array[i]
                array[i] = array[i+step]
                array[i+step] = tmp
        step = int(step // 1.247)