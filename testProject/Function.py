

# def greet():
#     print("Hello")
#     print("Good morning")

# def add(x,y):
#     c = x+y
#     return c

# greet()
# result = add(5,4)
# print(result)

def update(x):

    print(id(x))

    x = 8
    print(id(x))
    print(x)

a = 10
print(id(a))
update(10)
print(a)