n, k = map(int, input().split())

score = list(map(int, input().split()))

advance = 0

for i in range(n):
    if score[i] >= score[k - 1] and score[i] > 0:
        advance += 1

print(advance)
