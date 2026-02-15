import string

l = input().lower()
L = string.ascii_lowercase

b = min((L.index(l[0])), (26-(L.index(l[0]))))
count = 0

for i in range(1, len(l)):
    letter = abs(L.index(l[i-1]) - L.index(l[i]))
    count += min(letter, (26-letter))

print(count + b)
