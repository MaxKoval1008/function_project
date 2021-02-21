def my_animal_generator():
    yield 'cow'
    for animal in ['cat', 'dog', 'bear']:
        yield animal
    yield 'whale'


my_generator = my_animal_generator()
print(next(my_generator))
print('------------')
print(next(my_generator))
print('------------')
for animal in my_generator:
    print(animal)
    # cow cat dog bear whale
