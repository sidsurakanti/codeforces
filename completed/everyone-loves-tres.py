#2035B

t = int(input())
for _ in range(t):
  n = int(input())
  if n % 2 < 1:
    sol = 3*((10**(n) - 1)//9) + 33 
    print(sol)
  else:
    print(-1 if n < 4 else 3*((10**(n) - 1)//9) + 3033)
    