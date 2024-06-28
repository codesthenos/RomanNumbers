import tools_is_roman_expression

def is_roman_expresion(string):
  return not tools_is_roman_expression.has_string_more_than_3_in_a_row(string) and tools_is_roman_expression.is_string_composed_by_correct_values(string) and tools_is_roman_expression.is_string_well_ordered(string)

def is_input_int(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def validate_user_input(value):
  user_input = ""
  if is_input_int(value):
    user_input = int(value)
  elif is_roman_expresion(value):
    user_input = value
  if user_input == "":
    return validate_user_input(input(f"{value} is not a correct number or roman expression,\nplease try again with something similar to '53782614' or 'M00M0MCCXII': "))
  return user_input