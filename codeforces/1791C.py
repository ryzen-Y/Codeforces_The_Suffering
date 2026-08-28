t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = n

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            ans -= 2
        else:
            break

    print(ans)
