class X:
    """static variables are defined here"""
    def m1(self):
        a = 10
        b = 20
        print a
        print b
    def modify(self):
        self.a = 100 
        self.b = 200
    def display(self):
        print self.a
        print self.b
x1 = X()
x1.m1()
x1.modify()
x1.display()
print(x1.a)
print(x1.b)
