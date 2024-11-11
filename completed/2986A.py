def solve():
  n, a, b = list(map(int, input().split()))
  coord = [0, 0]
  yur = {
    "N": [1, 1],
    "S": [1, -1],
    "E": [0, 1],
    "W": [0, -1],
  }
  moves = input()

  for _ in range(20*n+50):
    for dir in moves:
      match = yur[dir]
      coord[match[0]] += match[1]
      if coord == [a, b]:
        return print("YES")
  print("NO")

for _ in range(int(input())):
  solve()