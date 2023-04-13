

a = 10
print(id(a))

def something():
    a = 9

    a = 15
    
    x = globals()['a']
    print(id(x))


something()

print('out', a)