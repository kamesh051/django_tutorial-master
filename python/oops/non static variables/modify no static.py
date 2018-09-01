class X:
    """static variables are defined here"""
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print ("constructor")
    '''def modify(self):
        self.a = 100 
        self.b = 200'''
    def display(self):
        print self.a
        print self.b
x1 = X(10,20)

#x1.modify()
x1.display()
print(x1.a)
print(x1.b)
print " "

x2 = X(1000,2000)
#x2.modify()
x2.display()
