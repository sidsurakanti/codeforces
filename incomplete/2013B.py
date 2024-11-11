def solve():
  n = int(input())
  a = sorted(list(map(int, input().split())))
  print(a[-1] - (a[-2] - sum(a[:-2])))

for _ in range(int(input())):
  solve()