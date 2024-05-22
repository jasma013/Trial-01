class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

# Creating instances of the Dog class
dawa = Dog("dawa", "brown", 6)
nima = Dog("nima", "white", 3)
blacky = Dog("blacky", "Black", 2)

# Printing the details of each dog instance
print("Name:", dawa.name, "Color:", dawa.color, "Age:", dawa.age)
print("Name:", nima.name, "Color:", nima.color, "Age:", nima.age)
print("Name:", blacky.name, "Color:", blacky.color, "Age:", blacky.age)
