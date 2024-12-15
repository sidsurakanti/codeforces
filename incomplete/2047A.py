def solve():
  k = int(input())
  cases = list(map(int, input().split()))

  # iterations of sides of box till day_k
  s1 = [n**2 for n in range(1, k*10, 2)]
  
  count = 0
  sum = 0

  for c in cases:
    sum += c
    if sum in s1:
      count += 1
    
  print(count)

for _ in range(int(input())):
  solve()