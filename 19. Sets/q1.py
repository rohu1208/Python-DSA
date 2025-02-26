# Return a list of all unique elements
# order does not matter
my_list = [43, 54, "tohan", 43.5, 54]
# my_set = set(my_list) # o(n)

my_set = set()
# for i in range(0, len(my_list)):
#     my_set.add(my_list[i])
# print(my_set)  # {43, 43.5, 54, 'tohan'}

result = []
for num in my_set:
    result.append(num)
print(result)  # [43, 43.5, 54, 'tohan']
