class Dog():
    """Простая модель собаки"""
    def __init__(self,name,age):
        self.name = name    
        self.age = age
    def sit(self):
        """Собака садится по комманде"""
        print (f"{self.name} is now sitting")
    def roll_over(self):
        """Cобака перекатывается по команде"""
        print(f"{self.name} is now rolled over!")
class Human():
    def hello(name):
        print("I'm not a dog")
my_dog = Dog('willie',6)
print(f"My Dog's name is {my_dog.name}")
print(f"My Dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()
human = Human()
human.hello()
your_dog = Dog('lucy',3)
print(f"{your_dog.name} Age =  {your_dog.age}")
your_dog.roll_over()

#9.1
class Restaurant ():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe(self):
        print (f"{self.name} --- {self.type}")
    def open(self):
        print(f"Restaurant {self.name,self.type}is open")
restaurant = Restaurant("Kirill","pub")

#9.2
my_restaurant = Restaurant("Boris","cafe")
your_restaurant = Restaurant("Irina","restaurant")
restaurant.describe()
my_restaurant.describe()
your_restaurant.describe()

#9.3
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"Имя пользователя - {self.first_name}, Фамилия - {self.last_name}")
user = User("Кирилл", "Баранов")
user.describe_user()