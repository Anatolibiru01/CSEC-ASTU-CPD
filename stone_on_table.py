n = int(input())
s = input().strip()

k = 0
for i in range(1, n):
    if s[i-1] == s[i]:
        k += 1

print(k)
