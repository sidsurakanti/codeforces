# def solve():
#   N = int(input())
#   count = 0

#   for i in range(2, N+1):
#     P = len(str(i))
#     if chainRound(i, P) != round(i, P):
#       count += 1
#     # print(chainRound(i, P))
#     # print(round(i, P))
#   print(count)

def round(n, b):
  x = (n % 10**b) // 10**(b-1)
  c = 0
  if x >= 5: 
    c += (n + 10**b) // 10**b
  else: 
    c += n // 10**b
  return c * 10**b

def chainRound(n, b):
  d = n
  for i in range(1, b+1):
    d = round(d, i)
  return d

inputs = [int(input()) for _ in range(int(input()))]
maxN = max(inputs)

pref = [0]*(maxN+1)

for i in range(1, maxN+1):
  P = len(str(i))
  pref[i] = pref[i-1] + (chainRound(i, P) != round(i, P))

for k in inputs:
  print(pref[k])



