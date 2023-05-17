# function to reverse the digits of integers
# takes number as argument
def reverse_number(n, reverse_num=0):
    # using absolute value of number
    # as negative numbers lead to infinite loop
    n = abs(n)

    # running loop until number is reduced to 0
    while n:
        # calculate division and modulus in same function
        n, digit = divmod(n, 10)
        # digit= n% 10; n//= 10

        # multiplying reverse number value by 10 and adding the digit
        reverse_num *= 10
        reverse_num += digit

    # returning the reverse number
    return reverse_num


if __name__ == "__main__":
    print(3456754, "::", reverse_number(3456754))
