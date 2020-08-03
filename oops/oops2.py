#########################################
# Encapsulation
class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password
    
    def get_pwd(self):
        return self._password
    
###############################################

#################################################

# Inheritence

class Animal:
    def __init__(self, legs, has_tail):
        self.legs = legs
        self.has_tail = has_tail
        self.teeth = 32
    
    def walk(self):
        print("animal is walking")
    
    def eat(self):
        print("animal is eating")

class Fish(Animal):
    def __init__(self, legs, has_tail):
        super().__init__(legs, has_tail)
        self.fins = 2
    
    def walk(self):
        print("fish is walking")
    


class Dog(Animal):
    def __init__(self, legs, has_tail):
        super().__init__(legs, has_tail)
        self.tail = True
        self.life_span = 20
    
    def walk(self):
        print("dog jumps ")

class Random:
    def do_walking_and_eating(self, animal):
        animal.walk()
        animal.eat()

#######################################################

# Abstraction

class Animal:
    def __init__(self, legs, has_tail):
        self.legs = legs
        self.has_tail = has_tail
        self.teeth = 32
    
    def walk(self):
        raise NotImplementedError()

    def eat(self):
        raise NotImplementedError()

    def perform_daily_task(self):
        self.walk()
        self.eat()

class Cat(Animal):
    def __init__(self, legs, has_tail):
        super().__init__(legs, has_tail)
    
    def walk(self):
        print("stretches its body")
        print("cat will be walking")
    
    def eat(self):
        print("cat will be eating")
    
class Dog(Animal):
    def __init__(self, legs, has_tail):
        super().__init__(legs, has_tail)
        self.tail = True
        self.life_span = 20
    
    def walk(self):
        print("scratches his body")
        print("dog is walking")

    def eat(self):
        print("dog is eating")
    

###################################################
class Payment:
    def pay(self):
        raise NotImplementedError()

    def perform_payment(self):
        print("initiating payment")
        print("please wait for some minutes")
        self.pay()
        print("transaction is over")

class UPIPayment(Payment):
    def pay(self):
        print("upi: doing upi payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("credit_card: payment will be done")

class PaytmCardPayment(Payment):
    def pay(self):
        print("paytm: payment will be done")


##################################################
if __name__ == '__main__':

    payment = PaytmCardPayment()
    payment.perform_payment()
    
    # dog = Dog(4, True)
    # random = Random()
    # #dog.walk()
    # random.do_walking_and_eating(dog)

    # fish = Fish(0, True)
    # do_walking(fish)
    # # fish = Fish(0, True)
    # # fish.walk()

    # dog = Dog(4, True)
    # dog.perform_daily_task()

    # cat = Cat(4, True)
    # cat.perform_daily_task()
    
