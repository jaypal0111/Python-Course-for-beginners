class Mydemo:
    dw1 =  45

# print(Mydemo)

print(Mydemo.dw1)#45


d1 = Mydemo() # create object of the class
print(d1.dw1)#45


class Human:
    def __init__(yourname, fname, age):
        yourname.name = fname
        yourname.age =  age


    def __str__(self):
        return "done"
        print( "{self.name}({self.age})")

h1 =  Human('jay',29)
# # h1 =  Human() 
h1.name = 'Urmi'
h1.age = '32'
del h1.age
# # print(h1.name)
# # print(h1.age)
print(h1.name)#jay(29)


# # # class Animal:
# # #     pass