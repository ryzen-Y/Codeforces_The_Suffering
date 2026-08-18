n = int(input())

x = list(map(int, input().split()))
p = x[0]
x = x[1:]

y = list(map(int, input().split()))
q = y[0]
y = y[1:]

lst = x + y

if all(i in lst for i in range(1, n + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
