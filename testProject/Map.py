
def is_even(n):
    return n%2==0

nums = [2,3,6,8,6,8,2]

evens = list(filter(is_even,nums))

print(evens)