n = int(input())


for _ in range(n):
  diags = {}
  t = int(input())
  matrix = [[*map(int, input().split())] for _ in range(t)]
  for i in range(t):
    for j in range(t):
      diags[i-j] = min(diags.get(i-j, 0), matrix[i][j])
  
  total = 0
  for v in diags.values():
    total += -v
  
  print(total)


  