from pympler.asizeof import asizeof


def dobro():
    i = 0

    while True:
        yield i

x = dobro()
#    yield 1
#    yield 2
#    yield 3
    
#    for i in range(0, 5): --
#        yield i --


print(next(x))


# print(next(dobro()))  --


#print(type(dobro([1, 2])))

#print(next(dobro()))