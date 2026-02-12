#c++ solution: https://github.com/Anatolibiru01/Code_Force_Solutions/blob/master/800/A_word.cpp

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
