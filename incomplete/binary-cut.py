n = int(input())
for _ in range(n):
  s = input()
  # INCOMPLETE
  cuts = 1
  curr = s[0]
  i = 0

  while i < len(s):
    if curr != s[i]:
      if curr > s[i]:
        cuts += 1
      # cuts += (curr > s[i])
      elif curr < s[i] and cuts > 1:
        cuts += 1
      curr = s[i]
    i += 1
  print(cuts)

    # s = input()
    # if "".join(sorted(s)) == s:
    #     print("1")
    #     continue
    # curr = s[0]
    # cuts = 0
    # for i in range(1, len(s)):
    #     if s[i] != curr:
    #         cuts += 1
    #         curr = s[i]
    # print(cuts)
    #   # if "".join(sorted(s)) == s:
  #   print("1")
  #   continue