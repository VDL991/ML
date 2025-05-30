class Dog:
    # class attribute
    attr1 = "mammal"
    
    def__init__(self, name):
        self.name = name

#object instantiation
Ram = Dog("Ram")
Tommy = Dog("Tommy")

#Accessing class attributes 
print("Ram is a", Ram.__class__.attr1)
print("Tommy is also a", Tommy.__class__.attr1)

#Accessing instance attributes
print("My name is",Ram.name)
print("My name is", Tommy.name)

