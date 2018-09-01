def multiply(x):
    return x*x
def add(x):
    return x+x
myfunc = [multiply,add]
for i in range(5):
    value = list(map(lambda x:x(i),myfunc))
    print(value)
