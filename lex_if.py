def is_delim(c):
  return c == ' ' or c == '('

def main():
  code = input("Enter the code: ")
  token_count = 0
  i = 0

  while i < len(code):
      if code[i:i+2] == "if" and is_delim(code[i + 2]):
          print("if\n")
          token_count += 1
          i += 3
      elif code[i:i+5] == "while" and is_delim(code[i + 5]):
          print("while\n")
          token_count += 1
          i += 6
      elif code[i:i+3] == "for" and is_delim(code[i + 3]):
          print("for\n")
          token_count += 1
          i += 4
      else:
          i += 1

  print("total tokens:", token_count)

if __name__ == "__main__":
  main()
