t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    lst = sorted(lst)
    print(lst[1])
