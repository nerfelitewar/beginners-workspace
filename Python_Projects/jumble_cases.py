methods = str.upper, str.lower

def jumble(s):
  r = []
  n = 0
  for i in s:
    if not i.isalpha():
      r.append(i)
    else:
      r.append(methods[n](i))
      n = 1 if n == 0 else 0
  return ''.join(r)

print(jumble(input("Enter your text- ")))