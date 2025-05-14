def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def display_temperature_table(start, end):
    if start <= end:
        step = 1

    print("Celsius Fahrenheit")
    for celsius in range(start, end):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:6} {fahrenheit:10.2f}")

start = int(input("START: "))
end = int(input("END: "))

display_temperature_table(start, end)
