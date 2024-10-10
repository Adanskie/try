import sys
names = [
    ['Alice',"Bob",'Charlie'],
    ['David','Eve','Frank'],
    ['Grace','Heidi','Ivan'],
    ['Judy','Ken','Laura']
]

me = input("Find Alice : ") 

for name in names:
    for get_name in name:
        if me == get_name:
            names.pop([0][0])
            print("Alice remove")
            print(names)
            sys.exit()
        else:
            me = input("Enter A Name : ")
            names.append(me)
            print("Success Adding New Name")
            print(names)
            sys.exit()
