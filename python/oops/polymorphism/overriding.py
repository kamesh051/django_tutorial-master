class X(object):
    def m1(self):
        print "m1 of of x class"
    def m2(self):
        print "m2 of class x"
class Y(X):
    def m1(self):
        super(Y,self).m1()
        print "m1 of class y"
    def m3(self):
        print "m3 of class y"
        
y1 = Y()
y1.m1()
y1.m3()
