# function to count the digits of integers
# takes number as argument and returns count of digits
def digit_count(n):
    # using absolute value of number
    # as negative numbers lead to infinite loop
    n = abs(n)

    # digit count initialized as zero
    digits = 0

    # running loop until number is reduced to 0
    while n:
        # dividing number by 10 until it becomes zero
        n //= 10

        # incrementing digit count by one for each iteration
        digits += 1

    # returning digit count
    return digits


if __name__ == "__main__":
    print(-239784, "::", digit_count(-239784))
    print(3456754, "::", digit_count(3456754))
