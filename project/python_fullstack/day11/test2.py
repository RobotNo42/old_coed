class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sex = 'boy'

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")


my_dog = Dog("LSY", 20)
my_dog.sit()
print(my_dog.sex)
my_dog.sex('girl')
print(my_dog.sex)
