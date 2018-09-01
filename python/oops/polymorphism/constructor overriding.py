class X(object):
    def __init__(self):
        print "constructor of x class"
class Y(X):
    def __init__(self):
        super(Y,self).__init__()
        print "constructor of y class"
        
y1 = Y()
