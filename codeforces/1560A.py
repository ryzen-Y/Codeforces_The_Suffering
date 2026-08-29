t = int(input())

for _ in range(t):
    k = int(input())

    count = 0
    i = 1

    while count < k:
        s = str(i)

        if i % 3 == 0 or s[-1] == '3':
            i += 1
            continue

        count += 1

        if count == k:
            print(i)

        i += 1
