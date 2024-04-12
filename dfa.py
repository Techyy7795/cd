def main():
  input_string = input("Enter string: ")
  state = 0

  i = 0
  while i < len(input_string):
      if state == 0 and input_string[i] == 'a':
          state = 1
          i += 1
      elif state == 0 and input_string[i] == 'b':
          state = 4
          i += 1
      elif state == 1 and input_string[i] == 'a':
          state = 2
          i += 1
      elif state == 1 and input_string[i] == 'b':
          state = 3
          i += 1
      elif state == 2 and input_string[i] == 'a':
          state = 2
          i += 1
      elif state == 2 and input_string[i] == 'b':
          state = 3
          i += 1
      elif state == 3 and (input_string[i] == 'a' or input_string[i] == 'b'):
          state = 4
          i += 1
      elif state == 4 and (input_string[i] == 'a' or input_string[i] == 'b'):
          state = 4
          i += 1
      else:
          print("Invalid string")
          return

  if state == 1 or state == 3:
      print("String accepted")
  else:
      print("String rejected")

if __name__ == "__main__":
  main()
