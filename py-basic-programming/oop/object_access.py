class Pay:
    def __init__(self):
        self.day = 25
        self.__money = 0

    def changeMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money


p = Pay()

print(p.day)
print(p.getMoney())
p.changeMoney(20000)
print(p.getMoney())
