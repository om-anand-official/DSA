def bubble_sort(ls):
    n = len(ls)
    for i in range(n):
        for j in range(i, n):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
    return ls


if __name__ == "__main__":
    ls = [62, 53, 59, 83, 15, 57, 11, 22, 88, 62, 26, 41, 7, 93, 87, 26, 43, 11, 48, 74]
    print(ls)
    print(bubble_sort(ls))
