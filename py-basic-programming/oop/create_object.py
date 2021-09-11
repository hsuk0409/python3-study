class Bike:
    def __init__(self):
        self.color = "black"
        self.weight = 3
        self.speed = 0

    def drive(self):
        self.speed += 1
        self.print_speed()

    def brake(self):
        self.speed -= 1
        self.print_speed()

    def print_speed(self):
        print('현재 스피드: {0}'.format(self.speed))


myBike = Bike()
otherBike = Bike()

print('myBike == otherBike => {}'.format(myBike == otherBike))
print(myBike)
myBike.drive()
myBike.drive()
myBike.drive()
myBike.brake()
