# function to list all factors
# takes number as argument
def factors(n):
    # every number has 2 factors 1 and itself
    ls = [1, n]

    # looping from 2 to square root of number
    # to check divisibility
    for i in range(2, int(n**0.5) + 1):
        # divisible numbers appended to list
        if n % i == 0:
            ls.append(i)
            # if there is another factor(not for square)
            if n // i != i:
                ls.append(n // i)
    return ls


if __name__ == "__main__":
    print(3456754, "::", factors(3456754))
    print(7532358, "::", factors(7532358))
    print(197, "::", factors(197))
