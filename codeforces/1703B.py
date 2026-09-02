t = int(input())
for _ in range(t):
    n = int(input())
    s = input().upper()

    first = set(s)
    diff = len(s) - len(first)
    ballon = len(first) * 2 + diff
    print(ballon)
