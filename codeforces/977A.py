n, k = map(int, input().split())

for i in range(k):
    digit = n % 10
    if digit > 0:
        n -= 1
    else:
        n //= 10
print(n)
