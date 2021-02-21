class Car:
    __last_model = None

    def __init__(self, model):
        self.model = model
        Car.__last_model = model

    @staticmethod  # мы не можем обратиться к атрибутам класса, поэтому значение указывается в скобках, model - название аргумента
    def is_model_ok(model):
        return len(model) > 3


print(Car.is_model_ok('abc'))
