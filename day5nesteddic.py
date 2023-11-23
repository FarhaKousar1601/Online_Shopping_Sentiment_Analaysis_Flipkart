#dictionary Nested
Number = {
            'one':1,
            'two':2,
            'three':3,
            'four':4,
            
            }

for value in Number.values():
           print(value)
           
#remove the value and add:pop,pop.item,clear,del dict
Number.pop("two")
print(Number)

Number.clear()
print("Dictionary after using clear:", Number)

