#interview question
# Fizz- Bus
'''
Ask a number from user 
if num divisible by 2 --> Fizz print
if num divisible by 3 --> Buzz print
if num divisible by both 2 and 3 --> Fizz Buzz print
else:
FIZZFIZZBUZZBUZZ
'''
num= int(input())
if num % 2 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num%2==0:
    print("Fizz")
elif num%3==0:
    print("Buzz")
else:
    print("FIZZFIZZBUZZBUZZ")
    
# write and condition on top else it will invalid for number 6