class X(object):
    def __init__(self,a):
        self.a=a
    def __str__(self):
        return self.a
    def m1(self):
        print "in m1 of class x"
        
class Y(X):
    def __init__(self):
        super(Y,self).__init__("kamesh")
        print "in constructor of y class"
    def m1(self):
        super(Y,self).m1()
        print "in m1 of y class"
        
x1 = X("reddy")
print x1
l = x1.__str__()
print l

y1 = Y()
print y1
k = y1.__str__()
print k
y1.m1()
