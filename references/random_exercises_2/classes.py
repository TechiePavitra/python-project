# defined class called Dog
class Dog:
    """Generates information about dog."""
    
    # Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Methods
    def bark(self):
        """Stimulates barking"""
        print(f"{self.name} is barking.")
    
    def sit(self):
        """Stimulates that dog is sitting"""
        print(f"{self.name} is sitting.")
   
    def roll_over(self):
        """Stimulates that dog is rolled over"""
        print(f"{self.name} rolled over.")

# Creating multiple instances         
my_dog = Dog("Willie", 5)
your_dog = Dog("Lucy", 3)


print(f"My Dog's name is {my_dog.name}")
print(f"My Dog is {my_dog.age} years old.")
my_dog.bark()

print(f"\nYour Dog's name is {your_dog.name}")
print(f"Your Dog is {your_dog.age} years old.")
your_dog.roll_over()