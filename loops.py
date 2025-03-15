time = 13


#while loop:

while time < 24:
    #print(time)
    # if time == 20:
    #     #break
    #     print('this is special case with 20')
    #     continue
    print(time)
    
    time +=1


print('===================================')
time2 = 13
while time2 < 18:
    print(time2)
    time2 +=1

else:
    print('time is not less than 18 now!')
    print(time2)


#for loop:

fruite = ["apple","banana","mengo","cherry"]

for fname in fruite:
    if(fname=='banana'):
        print('this is banana fruit')
        continue
    
    print(fname)