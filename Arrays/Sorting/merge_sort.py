def merge_sort(ls, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(ls, low, mid)
    merge_sort(ls, mid + 1, high)
    return merge(ls, low, mid, high)


def merge(ls, low, mid, high):
    left, right = low, mid + 1
    tmp = []

    while left <= mid and right <= high:
        if ls[left] <= ls[right]:
            tmp.append(ls[left])
            left += 1
        else:
            tmp.append(ls[right])
            right += 1

    while left <= mid:
        tmp.append(ls[left])
        left += 1

    while right <= high:
        tmp.append(ls[right])
        right += 1

    for i in range(low, high + 1):
        ls[i] = tmp[i - low]

    return ls


if __name__ == "__main__":
    ls = [62, 53, 59, 83, 15, 57, 11, 22, 88, 62, 26, 41, 7, 93, 87, 26, 43, 11, 48, 74]
    print(ls)
    print(merge_sort(ls, 0, len(ls) - 1))
