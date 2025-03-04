# Multiple inheritance.py
# Father class
class Father:
    def __init__(self):
        self.father_name = "John"

    def show_father(self):
        return f"Father: {self.father_name}"


# Mother class
class Mother:
    def __init__(self):
        self.mother_name = "Emma"

    def show_mother(self):
        return f"Mother: {self.mother_name}"


# Child class (inherits from both Father and Mother)
class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Alice"

    def show_child(self):
        return f"Child: {self.child_name}"


# Creating an instance of Child class
child = Child()

# Printing the outputs
print(child.show_father())  # Output: Father: John
print(child.show_mother())  # Output: Mother: Emma
print(child.show_child())  # Output: Child: Alice
