def create_cubes(n):
    return range(n)


print(list(create_cubes(10)))

def simple_gen():
    for x in range(3):
        yield(x)


print(next(simple_gen()))
print(next(simple_gen()))