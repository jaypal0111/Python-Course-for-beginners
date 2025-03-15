# Set: It is collection unordered(unindexed), unchangeable and no duplicates elements
# remove note: it will give you an error if item is not occured or exist
# discard note: if item is not occured or exist, it will not raise an error.
# pop note: Set is unordered, so if you use pop() method, you will not able to know which item/element will remove from set. 


myset = {"bmw","audi","duster","mini"}
youset = {"b1","b2","b3"}

num1 = {2,3,4,"b1"}

print(myset)

myset.update(youset)

print(myset)

combo = youset.union(num1)
print(combo)

myset.update(num1)

print(myset)

a1 = {"apple","banana","cherry"}
a2 = {"ibrainers","IBM","apple"}

a1.intersection_update(a2)

a3  = a1.intersection(a2)

print(a1)
print(a3)
a3 = {"apple","banana","cherry"}
a3.symmetric_difference_update(a2)

print(a3)