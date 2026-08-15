t = int(input())
lst = list(map(int, input().split()))
flag = False

for i in range(t):
    if lst[i] == 1:
        flag = True
        break

if flag:
    print("HARD")
else:
    print("EASY")
