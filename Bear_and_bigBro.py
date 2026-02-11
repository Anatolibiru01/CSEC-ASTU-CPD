n, m = map(int, input().split())
 
k = 0
while (n <= m):
    n = 3*n
    m = 2*m
    k += 1
 
print(k)
