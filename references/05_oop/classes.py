class Dog:
    """A Simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    
    def bark(self):
        """Simulate a dog barking in response to a command."""
        print(f"{self.name} is now barking!")

#                                             ~~~ DOCUMENTATION IN MY WORDS ~~~ 
# What classes does?
# some objects has common behaviors like dog has a action called roll over,
# every dog can bark, which is design, and this design is called a class,
# Classes are very great for making a maintainable systems and programs,
# Classes saves time and effort in programming,
# Notice that Dog is capitalized, because capitalized names refer to classes in Python
# A function that is part of class is called "Method",
# A method is simply a function that belongs to a class/object.
# Most function concepts still apply to methods.

# What __init__ or initializer (or constructor of classes) does?
# __init__ is like a form which collects data, very specific data,
# We have two data, first one is very specific, 
# Every Dog has a specific name and age, it can differ dog to dog,
# I.e: first dog name is rocky and other one is harry, both has different data,
# The Specific Data is called properties/attributes/data
# but has some common action or behaviors, like bark, roll over and sit,
# which is second part of the code

# Second Part is Dog's behaviors which are common among all dogs,
# Every new dog created from this class will automatically have these behaviors.
# Class and Objects make Python code more Reusable, Maintainable and flexible.

# What is self?
# Self means current object in class,
# Imagine you have three dogs: Rocky, Harry, Bruno and you command dog to sit!
# which dog will going to sit?: rocky? harry? or bruno?
# How python will understand, whom we are talking about?
# When we are working on Rocky, the self means self = Rocky or, when we're working on Harry, self = Harry
# In simple words, self = this_dog  

# Confusing Syntax explaination
# self.name = name
# here the self is attached with name using a dot,
# self is a object and name is a attribute because it is attached using dot, it can be a method,
# but method has parentheses ()
# attribute means our data, that is specific