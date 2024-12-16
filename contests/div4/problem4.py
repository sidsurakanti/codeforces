def solve():
  n = int(input())
  a = [*map(int, input().split())]
  sol = []

  

#   for i in range(n):
#     sol.append(str(mode(a[:i+1])))

#   print(" ".join(sol))

# def mode(arr):
#   modes = []
#   tr = []

#   for i in set(arr):
#     modes.append(arr.count(i))
#     tr.append(i)
  
#   print(tr, modes)
  
#   return tr[modes.index(max(modes))]
#   # if modes.count(max(modes)) > 1:
#   #   return [tr[i] for i in range(len(modes)) if modes[i] == max(modes)]
#   # else:
#   #   return [max(modes)]


for _ in range(int(input())):
  solve()
