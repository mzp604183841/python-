from car import Car

my_tesla = Car('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())

my_tesla.odometer_reading = 23
my_tesla.read_odometer()

my_tesla.update_odometer()
