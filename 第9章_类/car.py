"""写一个汽车类，放在一个文件（模块中）"""

class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('this car has' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, milage):
        if milage >= self.odometer_reading :
            self.odometer_reading = milage
        else :
            print("you can't roll back an odometer ~")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
