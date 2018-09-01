def charPyramid(n):
    var = 1
    for i in range(0,n):
        
        for j in range(0,i+1):
            
            print (j),
            j += 1
        print ("\r")
n = input("pyramid size")
p = int(n)
charPyramid(p)
