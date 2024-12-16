def solve():
  n, k = map(int, input().split())
  b = [0]*k

  for _ in range(k):
    i, c = map(int, input().split())
    b[i-1] += c

  print(sum(sorted(b)[:-(n+1):-1]))

  # b = dict()

  # for _ in range(k):
  #   b_i, c_i = map(int, input().split())
  #   if b_i in b.keys():
  #     b[b_i] += c_i
  #   else:
  #     b[b_i] = c_i

  # shelved = sorted(list(b.values()))
  # max = sum(shelved[:-(n+1):-1])
  # print(max)

for _ in range(int(input())):
  solve()