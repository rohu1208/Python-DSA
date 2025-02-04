"""
Number Palindrome or not
"""

num = int(input("enter n ="))
n = num
ans = 0
while n > 0:
    last_digit = n % 10
    ans = (ans * 10) + last_digit
    n = n // 10

if n == ans:
    print("number is palindrome")
else:
    print("number is not palindrome")
