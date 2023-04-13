

a = 10

def something():
    global a
    a = 15
    print('in', a)


something()

print('out', a)