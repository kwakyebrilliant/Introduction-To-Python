from array import *

# vals = array('i',[5,9,-8,4,2])

# for e in vals:
#  print(vals[e])

arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search"))