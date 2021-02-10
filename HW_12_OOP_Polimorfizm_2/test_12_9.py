class Car:
    last_model = None  #атрибут класса

    def __init__(self, model):
        self.last_model = model
        Car.last_model = model  #перезаписывает атрибут для введенного значения


car1 = Car('A')
print(Car.last_model)

car2 = Car('B')
print(Car.last_model)
print(car1.last_model)
