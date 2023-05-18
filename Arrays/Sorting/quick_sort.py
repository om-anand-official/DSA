def quick_sort(ls, low, high):
    if low < high:
        partition_index = partition(ls, low, high)
        quick_sort(ls, low, partition_index - 1)
        quick_sort(ls, partition_index + 1, high)

    return ls


def partition(ls, low, high):
    pivot = ls[low]
    left, right = low, high

    while left < right:
        while ls[left] <= pivot and left < high:
            left += 1
        while ls[right] > pivot and right > low:
            right -= 1
        if left < right:
            ls[left], ls[right] = ls[right], ls[left]
    ls[low], ls[right] = ls[right], ls[low]
    return right


if __name__ == "__main__":
    ls = [62, 53, 59, 83, 15, 57, 11, 22, 88, 62, 26, 41, 7, 93, 87, 26, 43, 11, 48, 74]

    print(ls)
    print(quick_sort(ls, 0, len(ls) - 1))
