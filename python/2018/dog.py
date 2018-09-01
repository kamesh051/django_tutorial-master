class Dog():
    def __init__(self):
        self.food = 'biscuits'
        print("dog constructor")
    def run(self,speed):
        if speed < 50:
            print("female dog")
        else:
            print("male dog")
    def run(self,speed,move):
        print("puppy dog")
        print(self.food)
'''class puppy(Dog):
    def run(self,speed):
        print("puppy dog")
        print(self.food)
class cat(puppy):
    def run(self,s):
        print("cat class method")'''

Dog().run(10)
