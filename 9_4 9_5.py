class Car (object):
    """docstring for Car """
    def __init__(self, make, model, year):
        super(Car , self).__init__()
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print (f'this car has {self.odometr_reading} miles on it.')
    def update_odometer (self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You cant roll back odometer")
    def increment_odometr (self,miles):
        self.odometr_reading += miles
my_new_car = Car('audi','a4',2019)
print (my_new_car.get_descriptive_name())

my_new_car.odometr_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_new_car.update_odometer(49)
my_new_car.read_odometer()

my_new_car.increment_odometr(10)
my_new_car.read_odometer()

#9.4
class Restaurant ():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    def describe(self):
        print (f"{self.name} --- {self.type}")
    def open(self):
        print(f"Restaurant {self.name,self.type}is open")
    def set_number_served (self,number):
        self.number_served = number
        return print (self.number_served)
    def increment_number_served (self,plus_number):
        self.number_served += plus_number
        print (self.number_served)
restaurant = Restaurant("Kirill","pub")
print(f"{restaurant.number_served}")
restaurant.set_number_served(5)
restaurant.increment_number_served(5)

#9.5
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"Имя пользователя - {self.first_name}, Фамилия -" 
                    f"{self.last_name}")
    def increment_login_attempts (self):
        self.login_attempts += 1
    def reset_login_attempts (self):
        self.login_attempts = 0
user = User("Кирилл", "Баранов")
user.describe_user()
while True:
    user.increment_login_attempts()
    print (user.login_attempts)
    if user.login_attempts == 10:
        user.reset_login_attempts()
        break
