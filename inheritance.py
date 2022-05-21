# inheritance is used in python is used to achieve maximum maintanability
class Mammal:
    def warmblodded(self):
        print('warm blooded animal')

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.warmblodded()
cat1 = Cat()
cat1.warmblodded()