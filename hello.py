print("Hello, IBRAINERS LTD!")

if 7 > 9:
    print("7 is less than 9!")
else:
    print("condition is false")

if 7 > 9:
 print("7 is less than 9!")
 print("i am on")

# this is comment
#dsgg
#bgh
""" this is multiline comment
as more than 
one line
"""
a = 3
b = "My name is jaypal" #test

print(a)
print(b)


x = str(6) # x will be '6'
y = int(6) # y will be 6
z = float(6) #z will be 6.0

print(x)
print(y)
print(z)

print(type((x)))
print(type((y)))
print(type((z)))


c =  8
C = "Cat"

name = "urmi"
NAME = "Jaypal"
# """
# firstname
# first_name :  Snake Case
# firstName : Camel case
# _first_name
# FIRSTNAME
# FirstNameTest : Pascal case


# 8test
# test-id
# test id

# """
print(c)
print(C)

print(name)
print(NAME)


s, d, f =  "dog","monkey","cat"

q = w = e =  "elephant"
print(s)
print(d)
print(f)

print(q)
print(w)
print(e)

fruits = ["mengo","apple","cherry"]

b,n,m = fruits

print(b)
print(n)
print(m)

test1 = "hi"
test2 = "Urmi"
test3 = "How are you?"
print(test1,test2,test3)

print(test1 + ' ' + test2+ ' ' + test3)

num12 = 12
num13 = 13
name5 = 'jay'
name4 = "Bhatt"

print(num12 + num13)

print(name5 , name4)

op1 = "test1"

def myfunc():
    print("I am doing test of global variable " + op1)

myfunc()


r1 = 1   #int
r2 = 3.1 #float
r3 = 2+5j  #complex

print(type(r1))
print(type(r2))

print(type(r3))

print(r3)

import random
print(random.randrange(1,4))

q1 = int(2) # q1 will be 2
q2 = int(2.5) # q2 will be 2
q3 = int("4") #q3 will be 4

print(q1)
print(q2)
print(q3)


a1 = float(2) # a1 will be 2.0
a2 = float(2.5) # a2 will be 2.5
a3 = float("4") #a3 will be 4.0
a4 = float("4.2") #a4 will be 4.2

print(a1)
print(a2)
print(a3)
print(a4)


z1 = str("j23") # z1 will be 'j23'
z2 = str(4) # z2 will be '4'
z3 = str(7.8) #z3 will be '7.8'
z4 = 'jay'
print(z1)
print(z2)
print(z3)
print(z4)

name1 = '''my name is jay, i am living in uk,
test jay hello
hye are you ok?'''
name2 =  """ my name is jay, i am living in uk,
test jay hello
hye are you ok? """
print(name1)
print(name2)

first_name = 'jaypal'

# print(first_name[1])

for letter in first_name:
    print(letter)

print(len(first_name))

st1 =  "my name is jay"

print("jay" in st1)

# if "jay" in st1:
#     print('Yes', 'jay is there.')

if "jay" not in st1:
    print('Yes', 'jay is not there.')
else:
    print('No','Jay is there')