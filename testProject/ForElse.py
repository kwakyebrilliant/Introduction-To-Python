nums = [12, 15, 18, 21, 26]

for num in nums:

    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")