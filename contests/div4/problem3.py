def solve():
  m, a, b, c = [*map(int, input().split())]
  total = 0
  if a <= m:
    total += a
    r1 = m-a
    if c > r1:
      total+=r1
      c -= r1
    else:
      total += c
      c = 0
  else:
    total += m

  if b <= m:
    total += b
    r2 = m-b
    if c > r2:
      total+=r2
      c -= r2
    else:
      total += c
      c = 0
  else:
    total += m
  

  print(total)


for _ in range(int(input())):
  solve()