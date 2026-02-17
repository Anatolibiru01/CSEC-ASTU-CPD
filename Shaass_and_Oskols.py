n = int(input())
birds = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    if len(birds) > 1:
        if x == 1:
            birds[1] += (birds[0] - y)
        elif x > 1 and x < n:
            birds[x] += (birds[x-1] - y)
            birds[x-2] += (y-1)
        else:
            birds[x-2] += (y-1)

        birds[x-1] = 0
    else:
        birds[x-1] = 0

for i in birds:
    print(i)
