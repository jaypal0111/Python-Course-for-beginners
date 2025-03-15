# Tuple : it is collection ordered, unchangeable, allow duplicate elements
# len(your_tuple),type(your_touple), datatypes as string, num or combo, 
# do all function practice same as list 
# you can not change the value of tuple once you assign because tuple is unchangeable
mytuple = ("bmw","audi","duster")


yourtuple =  tuple(("apple","banana","mengo","coconut")) # tuple(())

print(mytuple)
print(mytuple[1])
print(yourtuple)

# mytuple[0] = "Mini" # because tuple is unchangeable

# print(mytuple)


result1 =  list(mytuple)
result1[0] = 'Mini'
print(type(result1))
print(result1)

mynewTuple =  tuple(result1)

print(mynewTuple)

(car1, car2, car3) = mytuple

print(car1)
print(car2)
print(car3)


# (b1, *b2) = yourtuple    # need to check from yourend

#print(b1) # apple
# #print(b2) # ["banana","mengo","coconut"]

newcars = mytuple * 3

print(newcars)


