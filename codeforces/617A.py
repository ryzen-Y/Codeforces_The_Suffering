n = int(input())
count = 0

while n != 0:
    if n >= 5:
        n -= 5
        count += 1
    elif n >= 4:
        n -= 4
        count += 1
    elif n >= 3:
        n -= 3
        count += 1
    elif n >= 2:
        n -= 2
        count += 1
    else:
        n -= 1
        count += 1

print(count)
