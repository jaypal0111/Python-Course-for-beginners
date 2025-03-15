#__iter__() __next__()


#mytuple = ("a1","b1","c1")
#mytupleIt = iter(mytuple)

#print(next(mytupleIt))
#print(next(mytupleIt))
#print(next(mytupleIt))



class Mynumbers:
    def __iter__(self):
        self.n = 1
        return self
    
    def next(self):
        num  = self.n
        self.n += 1
        return num

m1 = Mynumbers()
numbers = iter(m1)



print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
