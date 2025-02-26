# my_tuple = (2, 4, 5, "rohan")
# print(my_tuple)
# print(type(my_tuple))
# print(my_tuple[3])

# # they are immutable
# my_tuple[3] = "sahil"  # Errpr
# # TypeError: 'tuple' object does not support item assignment

# Crazy que
my_tuple = (2, 4, 5, "rohan")
print(my_tuple)
print(id(my_tuple))
my_tuple = (2, 4, 5, "sahil")
print(my_tuple)
print(id(my_tuple))


# it will run bcz having diff. address
