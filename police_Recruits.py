n = int(input())
s = list(map(int, input().split()))

p = 0
c = 0

for e in s:
    if e > 0:
        p += e
    else:  # crime occurs
        if p > 0:
            p -= 1
        else:
            c += 1

print(c)

#this solution takes more than a hour and more than 4 submition. even it is a vibe code with copilet 
