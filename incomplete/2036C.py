# ANYA AND 1100

def solve():
  s = list(input())

  l = False
  for i in range(len(s) - 3):
    if s[i:i+4] == ["1", "1", "0", "0"]:
      l = i
  
  for _ in range(int(input())):
    idx, zo = input().split()
    idx = int(idx) - 1
    s[idx] = zo
    
    if l and (i < idx < i + 4):
      # print(s[i:i+4])
      print(["NO", "YES"]["1100" in "".join(s[l:l+4])])
    else:
      for i in range(len(s) - 3):
        if s[i:i+4] == ["1", "1", "0", "0"]:
          l = i
      print(["NO", "YES"][l])


for _ in range(int(input())):
  solve()