def selection_sort(ls):
    n = len(ls)
    for i in range(n - 1):
        min_ls = i
        for j in range(i, n):
            if ls[j] < ls[min_ls]:
                min_ls = j
        ls[min_ls], ls[i] = ls[i], ls[min_ls]
    return ls


if __name__ == "__main__":
    ls = [62, 53, 59, 83, 15, 57, 11, 22, 88, 62, 26, 41, 7, 93, 87, 26, 43, 11, 48, 74]
    print(ls)
    print(selection_sort(ls))
