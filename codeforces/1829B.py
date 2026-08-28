t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    max_space = 0

    for i in range(n):
        count = 0
        if lst[i] == 0:
            count += 1
            for j in range(i+1, n):
                if lst[j] != 0:
                    i = j
                    break
                count += 1
        max_space = max(max_space, count)
    print(max_space)
