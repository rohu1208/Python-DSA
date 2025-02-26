# Dictionary
# Dictionary is a collection of key-value pairs.
# Dictionary is mutable.
# Dictionary is unordered.
# Dictionary is indexed.
# Dictionary is written in curly brackets.
# hash map
# Dictionary is represented by {key:value}
my_dict = {"Physics": 90, "Chemistry": 80, "Maths": 70, 4: 5}
# key must be unique
# if key double then it will be overwritten by most recent value
print(my_dict)
print(type(my_dict))

my_dict2 = {"name": "John", "age": 30, "city": "New York", (1, 2, 3, 4): "tuple"}
print(my_dict2)
# it will work
# data type of key should be immutable
# value can be anything

my_dict3 = {"name": "John", "age": 30, "city": "New York", [1, 2, 3, 4]: "list"}
print(my_dict3)
# it will not work because list is mutable
# TypeError: unhashable type: 'list'
