# function to check armstrong number
# takes number as argument and returns list of all digits
def armstrong_number(num, s="Armstrong"):
    # using absolute value of number
    # as negative numbers lead to infinite loop
    n = abs(num)

    # sum the cube of every digit
    cube_sum = 0

    # running loop until number is reduced to 0
    while n:
        # calculate division and modulus in same function
        n, digit = divmod(n, 10)
        # digit= n% 10; n//= 10

        # adding cube of every digit
        cube_sum += digit**3

    # if Cube of all digits is equal to original number
    return s if num == cube_sum else "not " + s


if __name__ == "__main__":
    print(-239784, "::", armstrong_number(-239784))
    print(3456754, "::", armstrong_number(3456754))

# Armstrong Number : Adding Cube of all digits shall be equal to original number
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153
