"""
ask a number = 23456
print 2 3 4 5 6
or 
6 5 4 3 2 
"""

n = int(input(" n ="))
while n > 0:
    print(n % 10, end=" ")
    n = n // 10
