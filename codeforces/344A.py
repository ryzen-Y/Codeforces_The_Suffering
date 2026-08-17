n = int(input())

prev = input()
count = 1

for _ in range(n - 1):
    cur = input()

    if cur != prev:
        count += 1

    prev = cur

print(count)
