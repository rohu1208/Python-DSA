"""
ask a num from user = 20 
1 2 4 5 10 20
"""

num = int(input("Enter n"))
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
