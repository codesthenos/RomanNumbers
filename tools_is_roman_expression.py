from enum import Enum

class RomanNumbers(Enum):
  I      = 1
  IV     = 4
  V      = 5
  IX     = 9
  X      = 10
  XL     = 40
  L      = 50
  XC     = 90
  C      = 100
  CD     = 400
  D      = 500
  CM     = 900
  M      = 1000
  MV0    = 4000
  V0     = 5000
  X0     = 10000
  X0L0   = 40000
  L0     = 50000
  C0     = 100000
  C0D0   = 400000
  D0     = 500000
  M0     = 1000000
  M0V00  = 4000000
  V00    = 5000000
  X00    = 10000000
  X00L00 = 40000000
  L00    = 50000000
  C00    = 100000000
  C00D00 = 400000000
  D00    = 500000000
  M00    = 1000000000

def input_string_into_special_list(string):
  special_list = []
  max_token_lenght = max(len(token.name) for token in RomanNumbers)
  index = 0
  while index < len(string):
    found = False
    for token_length in range(max_token_lenght, 0, -1):
      if index + token_length <= len(string) and string[index:index+token_length] in RomanNumbers.__members__:
        special_list.append(string[index:index+token_length])
        index += token_length
        found = True
        break
    if not found:
      special_list.append(string[index])
      index += 1
  return special_list

def has_string_more_than_3_in_a_row(string):
  for roman_number in RomanNumbers:  
    if roman_number.name * 4 in string:
      return True
  return False

def is_string_composed_by_correct_values(string):
  for element in input_string_into_special_list(string):
    if element not in [e.name for e in RomanNumbers]:
      return False
  return True

def is_string_well_ordered(string):
  segments = input_string_into_special_list(string)
  last_value = float('inf')
  for segment in segments:
    value = RomanNumbers[segment].value
    if value > last_value:
      return False
    last_value = value
  return True