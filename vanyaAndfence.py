n, h = map(int, input().split())
a = list(map(int, input().split()))
 
count = 0
for _ in a:
    if h >= _:
        count += 1
    else:
        count += 2
 
print(count)
