class Car:
    __last_model = None

    def __init__(self, model):
        self.model = model
        Car.__last_model = model

    @classmethod  #метод конкретного класса
    def get_last_model(cls):
        return cls.__last_model


car1 = Car('A')
print(Car.get_last_model())
