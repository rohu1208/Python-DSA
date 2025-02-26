# return unique order matter
# so use dictionary -- Most optimal
my_list = [43, 54, "tohan", 43.5, 54]
my_dict = dict()
for i in range(0, len(my_list)):
    my_dict[my_list[i]] = 0
# {43, 54, 'tohan', 43.5

print(my_dict)
