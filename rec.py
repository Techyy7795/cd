def E():
  global cursor
  if T() and Eprime():
      return True
  return False

def T():
  global cursor
  if F() and Tprime():
      return True
  return False

def F():
  global cursor
  if cursor and cursor[0] == '(':
      cursor = cursor[1:]
      if E() and cursor and cursor[0] == ')':  # Added check for cursor not being empty
          cursor = cursor[1:]
          return True
  elif cursor and cursor[:2] == 'id':  # Added check for cursor not being empty
      cursor = cursor[2:]
      return True
  return False

def Eprime():
  global cursor
  if cursor and cursor[0] == '+':
      cursor = cursor[1:]
      return T() and Eprime()
  return True

def Tprime():
  global cursor
  if cursor and cursor[0] == '*':
      cursor = cursor[1:]
      return F() and Tprime()
  return True

if __name__ == "__main__":
  string = input("Enter the string: ")
  cursor = string

  if E() and not cursor:
      print("Accepted")
  else:
      print("Rejected")


# E –> E + T | T 
# T –> T * F | F 
# F –> ( E ) | id

# E –> T E’ 
# E’ –> + T E’ | e 
# T –> F T’ 
# T’ –> * F T’ | e 
# F –> ( E ) | id