def add(x):
    return x+x
def multiply(x):
    return x*x
def module(x):
    return x%2
def divide(x):
    return x/2
myfunc = [add,multiply,module,divide]
for i in range(10):
    k = map(lambda x:x(i),myfunc)
    print k
