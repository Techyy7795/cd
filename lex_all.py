import re

def is_identifier(token):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token))

def is_constant(token):
    return bool(re.match(r'^[0-9]+(\.[0-9]+)?$', token))

def is_operator(token):
    return token in ['+', '-', '*', '/', '=', '==', '!=', '>', '<', '>=', '<=']

def is_keyword(token):
    return token in ['if', 'else', 'while', 'for', 'int', 'float', 'char', 'return']
  
def is_delimiter(token):
  return token in [' ', '(', ')', '{', '}', '[', ']', ',', ';',':']

def lexical_analyzer(expression):
  tokens = expression.split()
  lexemes = []
  for token in tokens:
    if is_identifier(token):
        lexeme_type = 'Identifier'
    elif is_constant(token):
        lexeme_type = 'Constant'
    elif is_operator(token):
        lexeme_type = 'Operator'
    elif is_keyword(token):
        lexeme_type = 'Keyword'
    elif is_delimiter(token):
        lexeme_type = 'Delimiter'
    else:
        lexeme_type = 'Unknown'

    lexemes.append((lexeme_type, token))

  return lexemes



expression = input("Enter an expression: ")
result = lexical_analyzer(expression)
print("\nLexical Analysis Result:")
for lexeme in result:
  print(lexeme)
