def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j-1] < arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def insertion_sortV1(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr


def insertion_sortV2(arr):
    for end in range(len(arr)-1):
        i = end
        while i >= 0 and arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    return arr


print(insertion_sortV1([1, 5, 4, 3, 2]))
