#parameters
#non -default parameters
def add(a,b):
    c = a+b
    print c
add(10,20)
add(30,40)

#default parameters
def add(x,y=200):
    z= x+y
    print z
add(30,40)
add(10)


