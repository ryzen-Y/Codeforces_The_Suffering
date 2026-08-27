s = input()

new = ""

i = 0

while i < len(s):
    if s[i] == ".":
        new += "0"
        i += 1

    elif s[i] == "-" and s[i + 1] == ".":
        new += "1"
        i += 2

    elif s[i] == "-" and s[i + 1] == "-":
        new += "2"
        i += 2

print(new)
