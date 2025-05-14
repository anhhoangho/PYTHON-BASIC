def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def display_temperature_table(start, end, target_unit):
    if target_unit == 'F':
        print("Celsius Fahrenheit")
        if start <= end:
            step = 1
        for celsius in range(start, end):
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:6} {fahrenheit:10.2f}")
    elif target_unit == 'C':
        print("Fahrenheit Celsius")
        if start <= end:
            step = 1
        for fahrenheit in range(start, end):
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:6} {celsius:10.2f}")
    else:
        print("Invalid target unit. Please enter 'C' or 'F'.")


target_unit = input("Enter the target unit ('C' or 'F'): ").upper()

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

display_temperature_table(start, end, target_unit)