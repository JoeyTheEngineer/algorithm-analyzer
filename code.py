def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


input = [1,2,3,4,5]
insertionSort(input)
