# function to check whether a number is prime or not
# takes the number as argument
def check_prime_number(n):
    # if number is less than 2 then it is invalid
    if n < 2:
        return "Invalid Number"

    # for number greater than or equal to 2
    for i in range(2, int(n**0.5) + 1):
        # if number is divisible by any other number
        # between 2 to its square root
        if n % i == 0:
            return "not Prime"
    return "Prime"


if __name__ == "__main__":
    print(3456754, "::", check_prime_number(3456754))
    print(7532357, "::", check_prime_number(7532357))
    for i in range(200):
        print(i, "::", check_prime_number(i))
