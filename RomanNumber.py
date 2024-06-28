import tools_is_roman_expression
import tools_RomanNumbers

class NumberintoRomanNumber():

  def __init__(self, user_input):
    self.user_input = user_input
    self.validated_user_input = self.get_validated_user_input()
    self.number = self.get_number()
    self.roman_expression = self.get_roman_expression()

  def __str__(self):
    return self.roman_expression
  
  def __repr__(self):
    return self.__str__()

  def __eq__(self, other):
    if isinstance(other, NumberintoRomanNumber):
      return self.number == self.number
    return False

  def __hash__(self):
    return hash(self.number)

  def get_validated_user_input(self):
    return tools_RomanNumbers.validate_user_input(self.user_input)
  
  def get_number(self):
    if type(self.validated_user_input) == str:
      roman_expression_list = tools_is_roman_expression.input_string_into_special_list(self.validated_user_input)
      result = sum(tools_is_roman_expression.RomanNumbers[element].value for element in roman_expression_list)
    else:
      result = self.validated_user_input
    return result
  
  def get_roman_expression(self):
    if type(self.validated_user_input) == int:
      num = self.validated_user_input
      roman_expression_string = ''
      sorted_roman_numbers = sorted(tools_is_roman_expression.RomanNumbers, key=lambda x: x.value, reverse=True)
      for roman_number in sorted_roman_numbers:
        while num >= roman_number.value:
          roman_expression_string += roman_number.name
          num -= roman_number.value
      result = roman_expression_string
    else:
      result = self.validated_user_input
    return result
  
  def __add__(self, other):
    return NumberintoRomanNumber(self.number + other.number)

  def __sub__(self, other):
    return NumberintoRomanNumber(self.number - other.number)

  def __mul__(self, num=1):
    return NumberintoRomanNumber(self.number * num)

  def __floordiv__(self, num=1):
    return NumberintoRomanNumber(self.number // num)

uno = NumberintoRomanNumber(1)
dos = NumberintoRomanNumber("II")
tres = uno + dos
otro_uno = dos - uno
print(f"{uno} + {dos} = {tres}")
print(f"{dos} - {uno} = {otro_uno}")
print(f"{dos} * 3 = {dos * 3}")
print(f"{tres} // 2 = {tres // 2}")
  #La calculadora va a ser tocando los metodos
  #__sub__ARREGLAR NUMEROS NEGATIVOS EXPRESION ROMANA
  #__mul__ ""
  #__floordiv__ "" Y 0DIVISION
  #Y COMPARACION DE > <
  #QUEDA TERMINAR ESTO