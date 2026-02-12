n = int(input())
a = list(map(int, input().split()))

s = list(map(str, sorted(a)))
print(" ".join(s))
