class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting ~")

    def roll_over(self):
        print((self.name.title()) + ' is rolled over ~')


# 将实例对象当做一个类的属性
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('this car has a ' + str(self.battery_size) + '-kwh battery ~')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            pass
        message = 'this car can go approximately ' + str(range)
        message += ' miles on a full charge '
        print(message)


class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectriCar('ll', 'bb', '2020')
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
