class x:
    def __init__(self,a):
        print "in constructor of x class"
class y(x):
    def __init__(self):
        print "in constructor of y class"
y1 = y(10)
