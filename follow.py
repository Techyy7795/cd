def follow(c):
  global m
  if a[0][0] == c:
      result.append('$')
      m += 1
  for i in range(numOfProductions):
      for j in range(2, len(a[i])):
          if a[i][j] == c:
              if a[i][j + 1:]:
                  first(a[i][j + 1])
              elif c != a[i][0]:
                  follow(a[i][0])

def first(c):
  global m
  if not c.isupper():
      result.append(c)
      m += 1
  for k in range(numOfProductions):
      if a[k][0] == c:
          if a[k][2] == '$':
              follow(a[k][0])
          elif a[k][2].islower():
              result.append(a[k][2])
              m += 1
          else:
              first(a[k][2])

if __name__ == "__main__":
  numOfProductions = int(input("Enter the no. of productions: "))
  a = []
  result = []

  print("Enter the productions (epsilon=$):")
  for _ in range(numOfProductions):
      a.append(input())

  while True:
      m = 0
      c = input("Enter the element whose FOLLOW is to be found: ")[0]
      follow(c)
      result = list(set(result))
      print(f"FOLLOW({c}) = {{ {' '.join(result)} }}")
      result.clear()
      if input("Do you want to continue (0/1)? ") != '1':
          break
