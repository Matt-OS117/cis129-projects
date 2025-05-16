# Class Pet
#Matt Fitzsimmons
#CIS129
#This is a class written to create an object and store data and output it back to the user.
#Have a good summer! 

class Pet:
    def __init__(self, name="", pet_type="", age=0):
        self.__name = name
        self.__type = pet_type
        self.__age = age

    # Mutators
    def setName(self, name):
        self.__name = name

    def setType(self, pet_type):
        self.__type = pet_type

    def setAge(self, age):
        self.__age = age

    # Accessors
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age


# The main buffet
def main():
    # Constructing the pet object
    animal = Pet()

    # Obtaining details about the pet from the user and storing their input
    input_name = input("Enter your pet's name :\n")
    animal.setName(input_name)

    input_type = input("\nEnter your pet's type :\n")
    animal.setType(input_type)

    input_age = int(input("\nEnter your pet's age :\n"))
    animal.setAge(input_age)

    #Simple output
    print(f"\nYour pet's name : {animal.getName()}\n")
    print(f"Your pet's type : {animal.getType()}\n")
    print(f"Your pet's age : {animal.getAge()}\n")



main()
