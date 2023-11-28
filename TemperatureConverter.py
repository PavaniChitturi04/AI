# Predicate to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get user input for Celsius temperature
celsius_temp = float(input("Enter a temperature in degrees Celsius: "))

# Get user input for the threshold temperature
threshold_temp = float(input("Enter a threshold temperature in degrees Fahrenheit: "))

# Convert Celsius temperature to Fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

# Output the conversion result
print(f"{celsius_temp}°C is equivalent to {fahrenheit_temp}°F")

# Check if the temperature is below the threshold
if fahrenheit_temp < threshold_temp:
    print(f"{fahrenheit_temp}°F is below {threshold_temp}°F")
else:
    print(f"{fahrenheit_temp}°F is not below {threshold_temp}°F")