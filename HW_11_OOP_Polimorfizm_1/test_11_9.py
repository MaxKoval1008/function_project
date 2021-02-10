class city:
    def __init__(self):
        self.__address = 'Minsk'

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


town = city()
print(town.get_address())
town.set_address('Grodno')
print(town.get_address())

