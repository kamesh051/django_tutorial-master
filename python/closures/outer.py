def outer(a):
    print(a)
    def inner(b):
        print(b)
        def deep(c):
            print(c)
        return deep
    return inner
var  = outer("kamesh")
var1 = var("ksr")
var1("nvsr")
del outer,var,var1
