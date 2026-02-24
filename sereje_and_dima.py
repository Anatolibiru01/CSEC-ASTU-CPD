n = int(input())
card = list(map(int, input().split()))
ser = 0
dima = 0
turn = True

for i in range(n):
    extrem = max(card[0], card[-1])
    if turn:
        ser += extrem
        turn = False
    else:
        dima += extrem
        turn = True
    card.remove(extrem)

print(ser, dima)
