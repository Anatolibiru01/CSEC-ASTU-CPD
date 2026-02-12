# anatoli01
for _ in range(5):
    m = list(map(int, input().split()))
    if 1 in m:
        i = _ + 1
        j = m.index(1) + 1
        break

k = abs(3-i) + abs(3-j)
print(k) 
