
#pop,remove,clear,insert,reverse,
# home work as extend, remove, copy, count, sort

color = ["black","yellow","white","green"]

print(color[1])
print(len(color))


for colorName in color:

    if(colorName == 'green'):
        color.remove(colorName)
    
    print(colorName)

color.append('pink')

# print(color)

# color.pop(4)
# color.remove("green")

# color.remove("green")

# color.clear()

color.insert(2,"red")

print(color)

color.reverse()

print(color)