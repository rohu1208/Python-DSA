# make function return true if number is even, false if odd
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    return False


# def even_or_odd(number: int) -> bool:

#     return number % 2 == 0


# print(even_or_odd(2))  # True
# print(even_or_odd(3))  # False
print(is_even(2))  # True
