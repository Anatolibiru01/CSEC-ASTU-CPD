#c++ solution:  

import string
s = input()

cU = 0
for i in s:
    if i in string.ascii_uppercase:
        cU += 1
if (len(s) - cU) < cU:
    print(s.upper())
else:
    print(s.lower())
