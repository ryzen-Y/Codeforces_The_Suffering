n = int(input())
lst = list(map(int, input().split()))

max_pos = lst.index(max(lst))
min_pos = n - 1 - lst[::-1].index(min(lst))

ans = max_pos + (n - 1 - min_pos)

if max_pos > min_pos:
    ans -= 1

print(ans)
