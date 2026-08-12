t = int(input())
for i in range(t):
    s = input()
    n = len(s)

    if n > 10:
        n = n - 2
        s = s[:1] + str(n) + s[-1:]
    print(s)
