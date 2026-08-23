n = int(input())
lst = list(map(int, input().split()))

police = 0
crime = 0

for i in lst:
    if i > 0:
        police += i
    else:
        if police > 0:
            police -= 1
        else:
            crime += 1

print(crime)
