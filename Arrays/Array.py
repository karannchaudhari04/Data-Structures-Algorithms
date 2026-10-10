from array import *

val = array('i', [1,2,3,4,5,6,7,8])

for x in val:
    print(x, end=" ")

print()
copyArray = array(val.typecode, (x for x in val))

for i in copyArray:
    print(i, end=" ")

