t = int(input())

sum = 0

for _ in range(t):
    a, b, c = map(int, input().split())

    if a + b + c > 1:
        sum += 1

print(sum)
