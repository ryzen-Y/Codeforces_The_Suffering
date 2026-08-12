t = int(input())
x = 0

for _ in range(t):
    op1 = input()

    if op1 == "++X" or op1 == "X++":
        x += 1
    else:
        x -= 1
print(x)
