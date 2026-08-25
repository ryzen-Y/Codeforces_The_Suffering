x = list(map(int, input().split()))

total = max(x)
x.remove(total)

a = (x[0] + x[1] - x[2]) // 2
b = (x[0] + x[2] - x[1]) // 2
c = (x[1] + x[2] - x[0]) // 2

print(a, b, c)
