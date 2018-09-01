class Test:
    a = 100
    def display(self):
        print("in display method")
class Child(Test):
    def details(self):
        self.b = 200
        print("in details method")
        print(Test.a)
        print(self.display())
y1 = Child()
y1.details()
main()
