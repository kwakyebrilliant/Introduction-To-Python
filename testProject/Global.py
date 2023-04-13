

a = 10

def something():
    a = 9

    a = 15
    
    x = globals()


something()

print('out', a)