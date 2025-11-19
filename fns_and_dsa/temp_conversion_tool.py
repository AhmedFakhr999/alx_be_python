FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

if __name__=='__main__':
    temp = float(input('Enter the temperature to convert: '))  # Use float instead of int for decimal values
    choice = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()  # Convert to uppercase
    
    if choice == 'C':
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif choice == 'F':
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    else:
        print(r'Invalid temperature. Please enter a numeric value.')