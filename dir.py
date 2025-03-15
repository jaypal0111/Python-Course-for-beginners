# ordered/indexed, changable and no duplicates 
# list [], tuples (),  set {a,b,c}, dir {"a1":"1","a2":"2"}
# len, update, pop, popitem, del, clear, dir_name.copy()/dict.dir_name, 
mycar = {

    "name" : "BMW",
    "color": "Black",
    "year" : 2022,
    "availablecol" : ["red","yellow","blue","white"]
}
mycar['name'] = 'audi'
print(mycar['name'])
print(mycar['color'])
print(mycar['year'])

print(mycar)
carname = mycar.get("name")

dirkeys = mycar.keys()
dirval = mycar.values()

print(carname)
print(dirkeys)
print(dirval)


q1 = mycar.items() # items method will return each item in a dir as tuples() in list[], [().(),()]

print(q1)

if "name" in mycar:
    print("Yes i got my car name ")
    print(mycar["name"])

mycar['doors'] = 4

print(mycar)

for carinfo in mycar:
    print(mycar[carinfo])

for carkey, carval in mycar.items():
    print(carkey,carval)

for carkey in mycar.keys():
    print(carkey)

mycar2 = dict(mycar)

print(mycar2)


# collection of directories inside one directory, its called nested Directories
myacademic = {
   
   "ssc_board" :{
     "result" : "pass",
     "year" : 2008

   },

   "hhc_board" :{
     "result" : "pass",
     "year" : 2010

   },

    "be_uni" :{
        "result" : "pass",
        "year" : 2014

    },

    "msc_uni" :{
     "result" : "pass",
     "year" : 2016

   },

}



print(myacademic)