n = int(input())
lst = list(map(int, input().split()))

max_pos = lst.index(max(lst))
min_pos = lst.index(min(lst))

# Move maximum to the front
ans = max_pos

# If max is before min, min shifts one position left
if max_pos < min_pos:
    min_pos -= 1

# Move minimum to the end
ans += (n - 1 - min_pos)

print(ans)
