# Grandparent class
class Grandparent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

    def show_grandparent(self):
        return f"Grandparent: {self.grandparent_name}"


# Parent class (inherits from Grandparent)
class Parent(Grandparent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name  # set

    def show_parent(self):
        return f"Parent: {self.parent_name}"


# Child class (inherits from Parent)
class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name

    def show_child(self):
        return f"Child: {self.child_name}"


# Creating an instance of Child class
child = Child("John", "Michael", "David")

# Printing the outputs
print(child.show_grandparent())  # Output: Grandparent: John
print(child.show_parent())  # Output: Parent: Michael
print(child.show_child())  # Output: Child: David
