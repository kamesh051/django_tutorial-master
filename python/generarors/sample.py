def myfunc():
    n = 1
    print("first")
    yield n
    n += 1
    print("second")
    yield n
    n += 1
    print("third")
    yield n
gen = myfunc()
try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except:
    print("StopIteration")
