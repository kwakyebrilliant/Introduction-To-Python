

def div(a, b):
    print(a/b)


def smart_div(func):

    def inner(a,b):

        if a>b:
            a,b = b,a
        return func()

div(4,2)