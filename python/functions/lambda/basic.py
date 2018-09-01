func = lambda a:a/2
p = func(152)
print(p)

def myfunc(x,square):
    sq = square(x)
    print(sq)
    cube = sq*x
    print(cube)
myfunc(4,lambda x:x*x)
