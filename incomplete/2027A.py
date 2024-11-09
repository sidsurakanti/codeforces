def solve():
  # FAILS TIME CONSTRAINTS TEST 5
  input()
  g = [*map(int, input().split())]
  # FIND L
  l = []
  for i in range(1, len(g)):
    if g[i] < g[i-1]:
      l.append(g[i-1] - g[i])
      g[i] = g[i-1]

  # print(l)
  # l = [332, 307, 284, 33, 0, 248, 285]
  total = 0
  while len(l) > 0:
    l = [*filter(lambda x: x > 0, l)]

    # translate down min number
    m = min(l) if l else 0
    l = [x-m for x in l]
    total += (len(l) + 1) * m

  print(total)

for _ in range(int(input())):
  solve()




# g = [344, 12, 37, 60, 311, 613, 365, 328, 675]
# # FIND L
# l = []
# for i in range(1, len(g)):
#   if g[i] < g[i-1]:
#     l.append(g[i-1] - g[i])
#     g[i] = g[i-1]

# print(l)

# # l = [332, 307, 284, 33, 0, 248, 285]
# total = 0
# while len(l) != 1:
#   l = [*filter(lambda x: x > 0, l)]
#   # translate down min number
#   m = min(l)
#   l = [x-m for x in l]
#   total += (len(l) + 1) * m

# print(total)