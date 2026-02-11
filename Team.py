n = int(input())
k = 0
for _ in range(n):
    m = sum(list(map(int, input().split())))
    if m >= 2:
        k += 1
print(k)
