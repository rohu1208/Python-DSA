"""
reverse number
"""

n = int(input("n = "))
ans = 0
while n > 0:
    last_digit = n % 10
    ans = ans * 10 + last_digit
    n = n // 10
print(ans)
