t = int(input())
n = input().strip()
 
nd = n.count("D")
na = t - nd
 
if nd == na:
    print("Friendship")
elif nd > na:
    print("Danik")
else:
    print("Anton")
