'''
print yes 
if number is divisible by 2 and 3
but should not be divisioble by 5
'''
# Solution
num = int(input("Enter num"))
if num%2==0 and num%3==0 and num%5!=0:
    print("Yes")
else:
    print("No")