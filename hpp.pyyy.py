c1, c2, c3, c4, c5 = map(int, input().split())
b = (c1 + c2 + c3 + c4 + c5) // 5
if b // 10:
    print('YES')
else:
    print("NO")