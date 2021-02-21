class Pet:

    def __init__(self):
        pass

    @staticmethod
    def get_random_name(name):
        return name[::-1], list(reversed(name))


print(Pet.get_random_name('abcde'))
