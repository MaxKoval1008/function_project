class MyErr(Exception):
    def __init__(self, mess='Zero cost'):
        super().__init__(mess)


class Book:
    def __init__(self, pages, year, author, cost):
        try:
            self.pages = pages
            self.year = year
            self.author = author
            self.cost = cost
            if type(pages) != int:
                raise TypeError('Pages is not int')
            if type(year) != int:
                raise TypeError('Year is not int')
            if type(author) != str:
                raise TypeError('Author is not str')
            if type(cost) != int:
                raise TypeError('Cost is not int')
            if year > 2021:
                raise ValueError('Error year')

            if cost == 0:
                raise MyErr

        except TypeError as te:
            print(te)

        except ValueError as ve:
            print(ve)

        except MyErr as err:
            print(f'cost is not valid - {err}')
        else:
            print('Data is correct')


a = Book('str', 2022, 'Author', 10)
b = Book(12, 'str', 'author', 10)
c = Book(12, 2000, 45, 10)
d = Book(12, 200, 'author', [])
e = Book(12, 3000, 'author', 10)
f = Book(12, 2000, 'author', 0)