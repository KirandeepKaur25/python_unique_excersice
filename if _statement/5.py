# Ask the user for a temperature. Then ask them what units, 
# Celsius or Fahrenheit,
#  the temperature is in. 
# Your program should convert the temperature 
# to the other unit. 
unit = input("is this in celsius or Fahrenheit? (C/F): ").upper()
if unit == 'C':
   converted_temp = (temp * 9/5) + 32
   print(f"{temp} is {converted_temp:.1f}F")
elif unit == 'F':
   converted_temp + (temp -32) * 5/9
   print(f"{temp} is {coverted_temp:.1f}C")
else:
   print("invalid unit. Please enter 'C' of Celsius or 'F' for Fahrenheit.")

