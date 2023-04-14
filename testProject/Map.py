

nums = [2,3,6,8,6,8,2]

evens = list(filter(lambda n: n%2==0 ,nums))

doubles = list(map(lambda n: n+2,evens))

print(evens)