def add(a,*b):
    print a
    print b
add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)


def add(*x,y):
    print x
    print y
add(y=10)
add(10,y=20)
add(10,20,y=30)
add(10,20,30,y=40)
