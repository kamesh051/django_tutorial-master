x = {"ntr":{1:"jai lava kusa",2:"janatha garage",3:"nannaku prematho"},
     "pvana kalyan":{1:"attharintiki daredi",2:"katamaa",3:"gabbarsingh"},
     "mahesh":{1:"srimanthudu",2:"spyder",3:"dukudu"}}
print x
for p in x:
    print p
    v = x.get(p)
    #print v
    for q,r in v.items():
        print q,r
