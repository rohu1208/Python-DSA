# function return yes is even
def is_even(n: int) -> str:
    if n % 2 == 0:
        return "Yes"
    return "No"


print(is_even(2))  # Yes
print(is_even(3))  # No


# ternary
def is_even(n: int) -> str:
    return "Yes" if n % 2 == 0 else "No"
