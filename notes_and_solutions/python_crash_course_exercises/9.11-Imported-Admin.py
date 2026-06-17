# Start with your work from Exercise 9-8 (page 173). 
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

from privileges_class import User, Privileges, Admin

owner = Admin("Pavitra", "Patil", "India", "techiepavitra@gmail.com")
guest01 = User("John", "Cohl", "Germany", "johncohl1986@hotmail.com")

# calling methods
owner.describe_user()
owner.privileges.show_privileges()

guest01.describe_user()
guest01.greet_user()