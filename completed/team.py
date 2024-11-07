n = 0
for _ in range(int(input())):
    x = [int(i) for i in input().split()]
    if sum(x) > 1: n += 1
print(n)
