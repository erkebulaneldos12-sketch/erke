class Vehicle:
    def move(self):
        print('Moving')

class Bike(Vehicle):
    def move(self): print('Bike')

Bike().move()
