# TASK: Write a function that converts between Celsius and Fahrenheit.

# Define a function that takes a float and a string parameter
# If unit is 'C', convert to Fahrenheit
# If unit is 'F', convert to Celsius
# Return a formatted string with the result
# Prompt the user for input and call the function
# Display the converted temperature

# Great the user
name = input("What is your name? ").strip()
print(f"Hello {name}!! This  is a Celsius and Fahrenheit converter.")

#
def temputure_converter():
    if temputure_scale == "C":
        Converted = (temputure_scale * 9/5) + 32
        print(f"{temputure_unit}°C is {Converted}°F")
        return
    elif temputure_scale == "F":
        Converted = (temputure_scale - 32) * 5/9
        print(f"")



        
# Ask the user what he wants to convert
temputure_scale = input("What do you want to convert? C or F")
temputure_unit= input("What is the ")
