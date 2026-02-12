t = int(input())

sets = []
for _ in range(t):
    n = input()
    sets.append(n)

j = sets[0]
count = 1

for i in sets:
    if j != i:
        count += 1
        j = i
print(count)
