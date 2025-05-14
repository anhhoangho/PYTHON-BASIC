# Hồ Hoàng Anh _ 22115054122103

import numpy as np
import matplotlib.pyplot as plt
import csv

# Lấy dữ liệu đầu vào
while True:
    month = {
        'jan': 0, 'feb': 1, 'mar': 2, 'apr': 3,
        'may': 4, 'jun': 5, 'jul': 6, 'aug': 7,
        'sep': 8, 'oct': 9, 'nov': 10, 'dec': 11
    }


    cities_rain = []
    cities_sun = []
    cities_temp = []

    rain = []
    sun = []
    temp = []


    with open('rainfall.csv', 'r') as file:
        doc = csv.reader(file)
        for row in doc:
            cities_rain.append(row[0].strip().capitalize())
            rain.append([float(x) for x in row[1:13]])


    with open('sunshine.csv', 'r') as file:
        doc = csv.reader(file)
        for row in doc:
            cities_sun.append(row[0].strip().capitalize())
            sun.append([float(x) for x in row[1:13]])


    with open('temperature.csv', 'r') as file:
        doc = csv.reader(file)
        for row in doc:
            cities_temp.append(row[0].strip().capitalize())
            temp.append([float(x) for x in row[1:13]])


    all_cities = list(set(cities_rain + cities_sun + cities_temp))


    print("\nWelcome to CLIP, the CLImate Plotter\n")
    print("loading the data... done!\n")

# Nhập dữ liệu
    while True:
        input_cities = input("choose the cities: ").strip().lower().split()
        selected_cities = []
        for city in input_cities:
            city_cap = city.capitalize()
            if city_cap in all_cities:
                selected_cities.append(city_cap)
            else:
                print(f"{city} is not a legal value (ignored)")

        if selected_cities:
            break
        else:
            print('Try Again')

    while True:
        input_data = input("choose the data: temp(erature) rain(fall) sun(shine hours) OR all: ").strip().lower().split()
        valid_data = {'temp', 'rain', 'sun'}
        selected_data = []
        if 'all' in input_data:
            selected_data = ['temp', 'rain', 'sun']
        else:
            for d in input_data:
                if d in valid_data:
                    selected_data.append(d)
                else:
                    print(f"{d} is not a legal value (ignored)")
        if selected_data:
            break
        else:
            print("Try again")

    while True:
        input_months = input("choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: ").strip().lower().split()
        selected_months = []
        if 'all' in input_months:
            selected_months = list(range(12))
        else:
            for m in input_months:
                if m in month:
                    selected_months.append(month[m])
                else:
                    print(f"{m} is not a legal value (ignored)")
        if selected_months:
            break
        else:
            print('Try again')

    print("-----------------------------------")

# Ghi dữ liệu và xuất file
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'Data Type'] + [list(month.keys())[m].capitalize() for m in selected_months])

        for city in selected_cities:
            print(f"Data for {city}:\n")

            if 'temp' in selected_data:
                if city in cities_temp:
                    idx = cities_temp.index(city)
                    print("Temperature:")
                    for m in selected_months:
                        print(f"{list(month.keys())[m].capitalize():<10}", end='')
                    print()
                    for m in selected_months:
                        print(f"{temp[idx][m]:<10.2f}", end='')
                    print()
                    values = [temp[idx][m] for m in selected_months]
                    min_val = min(values)
                    max_val = max(values)
                    avg_val = sum(values) / len(values)
                    print(f"Minimum occurs in {list(month.keys())[temp[idx].index(min_val)].capitalize()}: {min_val}")
                    print(f"Maximum occurs in {list(month.keys())[temp[idx].index(max_val)].capitalize()}: {max_val}")
                    print(f"Average value: {avg_val:.2f}\n")

                    row = [city, 'Temperature'] + [f"{temp[idx][m]:.2f}" for m in selected_months]
                    writer.writerow(row)
                else:
                    print("No temperature data for this city.\n")

            if 'rain' in selected_data:
                if city in cities_rain:
                    idx = cities_rain.index(city)
                    print("Rainfall:")
                    for m in selected_months:
                        print(f"{list(month.keys())[m].capitalize():<10}", end='')
                    print()
                    for m in selected_months:
                        print(f"{rain[idx][m]:<10.2f}", end='')
                    print()
                    values = [rain[idx][m] for m in selected_months]
                    min_val = min(values)
                    max_val = max(values)
                    avg_val = sum(values) / len(values)
                    print(f"Minimum occurs in {list(month.keys())[rain[idx].index(min_val)].capitalize()}: {min_val}")
                    print(f"Maximum occurs in {list(month.keys())[rain[idx].index(max_val)].capitalize()}: {max_val}")
                    print(f"Average value: {avg_val:.2f}\n")

                    row = [city, 'Rainfall'] + [f"{rain[idx][m]:.2f}" for m in selected_months]
                    writer.writerow(row)
                else:
                    print("No rainfall data for this city.\n")

            if 'sun' in selected_data:
                if city in cities_sun:
                    idx = cities_sun.index(city)
                    print("Sunshine:")
                    for m in selected_months:
                        print(f"{list(month.keys())[m].capitalize():<10}", end='')
                    print()
                    for m in selected_months:
                        print(f"{sun[idx][m]:<10.2f}", end='')
                    print()
                    values = [sun[idx][m] for m in selected_months]
                    min_val = min(values)
                    max_val = max(values)
                    avg_val = sum(values) / len(values)
                    print(f"Minimum occurs in {list(month.keys())[sun[idx].index(min_val)].capitalize()}: {min_val}")
                    print(f"Maximum occurs in {list(month.keys())[sun[idx].index(max_val)].capitalize()}: {max_val}")
                    print(f"Average value: {avg_val:.2f}\n")

                    row = [city, 'Sunshine'] + [f"{sun[idx][m]:.2f}" for m in selected_months]
                    writer.writerow(row)
                else:
                    print("No sunshine data for this city.\n")

            if 'rain' in selected_data or 'sun' in selected_data:
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

                if 'rain' in selected_data:
                    for city in selected_cities:
                        if city in cities_rain:
                            idx = cities_rain.index(city)
                            months_names = [list(month.keys())[m].capitalize() for m in selected_months]
                            values = [rain[idx][m] for m in selected_months]
                            ax1.plot(months_names, values, marker='o', linestyle='-', label=city)
                    ax1.set_title("Rainfall in Selected Cities")
                    ax1.set_xlabel('Month')
                    ax1.set_ylabel('Rainfall (mm)')
                    ax1.grid(True)
                    ax1.legend()

                if 'sun' in selected_data:
                    for city in selected_cities:
                        if city in cities_sun:
                            idx = cities_sun.index(city)
                            months_names = [list(month.keys())[m].capitalize() for m in selected_months]
                            values = [sun[idx][m] for m in selected_months]
                            ax2.plot(months_names, values, marker='o', linestyle='-', label=city)
                    ax2.set_title("Sunshine in Selected Cities")
                    ax2.set_xlabel('Month')
                    ax2.set_ylabel('Sunshine Hours')
                    ax2.grid(True)
                    ax2.legend()

                plt.tight_layout()
                plt.show()

    continue_input = input("Bạn có muốn tiếp tục không? (yes/no): ").strip().lower()
    if continue_input == 'yes':
        continue
    elif continue_input == 'no':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("Vui lòng nhập 'yes' hoặc 'no'.")

