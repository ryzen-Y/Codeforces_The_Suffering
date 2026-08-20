n = int(input())
note = 0

while n > 0:
    if n >= 100:
        note += n // 100
        n = n % 100
    elif n >= 20:
        note += n // 20
        n = n % 20
    elif n >= 10:
        note += n // 10
        n = n % 10
    elif n >= 5:
        note += n // 5
        n = n % 5
    else:
        note += n
        n = 0

print(note)
