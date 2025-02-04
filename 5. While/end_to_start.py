"""
ask start from user = 15
ask end from user = 3
15 to 3 print
"""

start = int(input("start"))
end = int(input("end"))

i = start
while i >= end:
    print(i, end=" ")
    i -= 1
