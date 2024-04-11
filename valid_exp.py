def is_valid_expression(e):
  paran_bal = 0  
  valid = True   # both of these are primary conditions to become valid expression

  for i in range(len(e)):
      if e[i].isalpha() and (i < len(e) - 1 and e[i + 1].isalpha()) \
              or e[i].isalnum() and (i > 0 and e[i - 1] == ')' or i < len(e) - 1 and e[i + 1] == '('):
          valid = False
          break

      if e[i] in '+-/*%':
          # Check if there is a valid operand on both sides of the operator
          if e[i - 1].isalnum() and e[i + 1].isalnum() \
                  or e[i - 1] == ')' or i < len(e) - 1 and e[i + 1] == '(':
              pass
          else:
              valid = False

      # Count opening and closing parentheses
      if e[i] == '(':
          paran_bal += 1
      elif e[i] == ')':
          paran_bal -= 1

  # Return True if the expression is valid and parentheses are balanced, otherwise return False
  return valid and paran_bal == 0


  # Prompt the user to enter an expression
expression = input("Enter expression: ")
  # Check if the expression is valid and print the result
if is_valid_expression(expression):
  print("Valid")
else:
  print("Invalid")
