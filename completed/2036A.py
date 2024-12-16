def solve():
  n = int(input())
  mel = list(map(int, input().split()))
  for i in range(n-1):
    if abs(mel[i] - mel[i+1]) not in [5, 7]:
      print("NO")
      return
  print("YES")
  
for _ in range(int(input())):
  solve()