def computeFirst(c):
  global m
  if not c.isupper():
      result.append(c)
      m += 1
  else:
      for i in range(numOfProductions):
          if productionSet[i][0] == c:
              if productionSet[i][2] == '$': # eplison production checking(RHS of production)
                  result.append('$')
                  m += 1
              elif productionSet[i][2].islower():
                  result.append(productionSet[i][2])
                  m += 1
              else:
                  computeFirst(productionSet[i][2])

if __name__ == "__main__":
  numOfProductions = int(input("How many number of productions? : "))
  productionSet = []
  result = []

  print("Enter productions:")
  for i in range(numOfProductions):
      productionSet.append(input())

  while True:
      m = 0
      c = input("\nFind the FIRST of: ")
      computeFirst(c)
      print("first of ",c, "=","{","".join(result),"}")
      result.clear()
      choice = input("Press 'y' to continue and 'n' to exit: ")
      if choice.lower() != 'y':
          break
