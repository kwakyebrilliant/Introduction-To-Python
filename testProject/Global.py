

a = 10
print(id(a))

def something():
    a = 9

    a = 15
    
    x = globals()['a']


something()

print('out', a)