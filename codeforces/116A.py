n = int(input())

current = 0
maximum = 0

for _ in range(n):
    a, b = map(int, input().split())

    current -= a
    current += b

    maximum = max(maximum, current)

print(maximum)
