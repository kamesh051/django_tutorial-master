class X:
    def __init__(self):
        print "constructor method implemeted"
    def __del__(self):
        print "object destruction started"
x1 = X()
x2 = x1
x3 = x2

del x1
del x2
del x3
