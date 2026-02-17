host = []
guest = []
for i in range(int(input())):
    hi, ai = map(int, input().split())
    host.append(hi)
    guest.append(ai)

uniform = 0
for i in host:
    uniform += guest.count(i)
print(uniform)
