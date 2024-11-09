def solve():
  x, y, k = map(int, input().split())
  c = min(x, y)
  a, b = [(0, 0), (c, c)]
  c, d, = [(0, c), (c, 0)]
  print(a[0], a[1], b[0], b[1])
  print(c[0], c[1], d[0], d[1])

for _ in range(int(input())):
  solve()