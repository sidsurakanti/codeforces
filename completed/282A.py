x = 0

for _ in range(int(input())):
  op = input()
  x += 1 if "++" in op else -1

print(x)