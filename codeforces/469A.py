n = int(input())

p = int(input())
x = list(map(int, input().split()))

q = int(input())
y = list(map(int, input().split()))

levels = set(x + y)

if all(i in levels for i in range(1, n + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
