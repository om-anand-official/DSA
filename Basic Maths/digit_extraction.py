# function to extract the digits of integers
# takes number as argument and returns list of all digits
def digit_extraction(n):
    # using absolute value of number
    # as negative numbers lead to infinite loop
    n = abs(n)

    # empty list to store the digits in RTL
    ls = []

    # running loop until number is reduced to 0
    while n:
        # calculate division and modulus in same function
        n, digit = divmod(n, 10)
        # digit= n% 10; n//= 10

        # appending all digits to list
        ls.append(digit)

    # list will have all numbers in RTL
    # reversing list to maintain the order of number LTR
    return ls[::-1]


if __name__ == "__main__":
    print(-239784, "::", digit_extraction(-239784))
    print(3456754, "::", digit_extraction(3456754))
