k = list(map(int, input().split()))
s = input()

calori = 0
for i in s:
    calori += k[int(i)-1]

print(calori)
