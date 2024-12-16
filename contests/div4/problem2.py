def solve():
  reflections = {
    "q":"p",
    "w": "w",
    "p": "q"
  }

  print("".join([reflections[i] for i in input()])[::-1])
1
for _ in range(int(input())):
  solve()