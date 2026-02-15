a, b, c, d = map(int, input().split())
s = input()

trials = {1: a, 2: b, 3: c, 4: d}
calori = 0
for i in s:
    calori += trials[int(i)]

print(calori)
