class X:
    """static variables are defined here"""
    a = 10
    b = 20
    def m1(self):
        print(X.a)
        print(X.b)
    def modify(self):
        X.a = 100
        X.b = 200
    def display(self):
        print X.a
        print X.b
x1 = X()
x1.m1()
x1.modify()
x1.display()
print(X.a)
print(X.b)
