"""
Ask start from user = 3

Ask end from user = 10

Total of all the numbers divisible by 2 and 7


"""

start = int(input("start"))
end = int(input("end"))
i = start
total = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        total += i
    i += 1
print(total)
