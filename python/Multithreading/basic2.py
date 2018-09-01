import threading
class X(threading.Thread):
    def run(self):
        for p in range(10):
            print "thread - 1"
class Y(threading.Thread):
    def run(self):
        for q in range(10):
            print "thread - 2"
x1 = X()
y1 = Y()
x1.start()
y1.start()
