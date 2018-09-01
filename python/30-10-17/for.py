def outer(f):
    print("outer function")
    def inner():
        print("inner function")
        f()
    return inner
@outer
def myfunc():
    print("my function")
myfunc()
