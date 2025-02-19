# only even
# even = [x for x in range(1, 10) if x % 2 == 0]
# print(even)


# make list of all primme 2 to 100
def prime(num) -> bool:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


result = [i for i in range(2, 101) if prime(i)]
print(result)
