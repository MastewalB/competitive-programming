def shellSort(array):
    sublistCount = len(array) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(array, startPosition,  sublistCount)
        print("After increments of size", sublistCount, "The list is", array)
        sublistCount = sublistCount // 2


def gapInsertionSort(array, start, gap):
    for i in range(start + gap, len(array), gap):
        currentValue = array[i]
        position = i

        while position > gap and array[position - gap] > currentValue:
            array[position] = array[position - gap]
            position = position - gap

        array[position] = currentValue


array = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(shellSort(array))
