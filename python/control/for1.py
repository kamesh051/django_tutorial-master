class Bank:
    """ """
    def __init__(self):
        print("in the constructor of Bank")
    def method(self):
        print("in method")
    def __del__(self):
        print("in the destructor of Bank")
x1 = Bank()
x1.method()
x1 = Bank()
