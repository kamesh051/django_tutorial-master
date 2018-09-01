import json
file = open ('employee')  
data = json.load(file)
mylist = data['employees']
for p in mylist:

    print(p['firstName']+' '+p['lastName'])
