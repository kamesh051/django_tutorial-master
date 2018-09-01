while True:
    print "enter 'x' to exit"
    terms = input("upto to how many terms?")
    if terms == 'x':
        break
    else:
        term = int(terms)
        a = 0
        b = 1
        count = 2
        if term < 0:
            print "enter positive numbers"
        elif term == 0:
            print a
        else:
            print a,",",b,",",
            while count < term:
                c = a+b
                print c
                a = b
                b = c
                count +=1
            print "\n"
