

# def greet():
#     print("Hello")
#     print("Good morning")

# def add(x,y):
#     c = x+y
#     return c

# greet()
# result = add(5,4)
# print(result)

def update(lst):

    print(id(lst))

    x = 8
    print(id(x))
    print(x)

lst = [10,20,30]
print(id(lst))
update(10)
print(lst)