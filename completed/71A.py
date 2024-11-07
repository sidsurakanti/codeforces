def solve():
  w = input()
  print(w[0] + f"{len(w)-2}" + w[-1] if len(w) > 10 else w)

for _ in range(int(input())):
  solve()