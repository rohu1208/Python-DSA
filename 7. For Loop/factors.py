"""Ask number to find factorial"""

"""Brut-Force // Better // Optimal"""
n = int(input("N = "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


print()
# Better Solution
for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, end=" ")
print(n)


print()

# Optimal Solution
