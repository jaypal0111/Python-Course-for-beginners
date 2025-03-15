""" 
Arithmatic : +,-,*,/,%,**,//
Assignment : =, +=, -=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=
Comparison : == ,!=,> , < ,>=, <=
Logical : and, or, not
Identity : is, is not
Membership :  in , not in
Bitwise operators : &, |, ^, >>, << """
# 64 32 16 8 4 2 1
#  0 0  0 0 0 0

x= 2
y=65
print(y//x)

"""x &= 3 """ 
# x = x & 4
"""print(x)    0011, 0100, 0111, 1111, 00000,10000 ,y00000, 1000000, 64,32,16,8,4,2,1 """
# print(x)
a = set('abc')
a ^=set('cbe')

# print(a)

#  1 0  0 0 0 0 0 0   

a |=set('cbe')
# y <<= 1
# print(y)

# print(a)

w = 12

# print((w > 11 and w < 20))


f1 = ["apple","mengo"]
f2 = ["apple","mengo"] 
f3 = f1


# print(f1 is not f3) # true

# print(f1 is not f2) # flase

print(f1 == f2) # true


print("banana" not in f1)