s = input()
t = input()

j = 0
for step in t:
    if step == s[j]: j += 1
print(j+1)
