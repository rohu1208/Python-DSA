"""
    List Comprehension
    =================
    it is also used to create list
    """

# result =[]
# for i in range(1,11):
#     result.append(i)
# print(result)

result = [i for i in range(1, 11)]
print(result)
print("-------------------")


print([i % 2 == 0 for i in range(1, 11)])
