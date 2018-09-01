
def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print "*",
        print "\r"
n = input("pyramid height")
pyramid(n)


def triangle(a):
    for b in range(a):
        print " "*(a-b-1)+"*"*(2*b+1)
a = input("pyramid height")
triangle(a)
