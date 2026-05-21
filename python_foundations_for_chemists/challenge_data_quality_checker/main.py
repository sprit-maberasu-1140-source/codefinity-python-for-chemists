def check_temperatures(temperatures):
    for temp in temperatures:
        if temp < 20 or temp > 30:
            warning = f"Warning: Temperature {temp}°C is out of range!"
            print(warning)

temps = [22.5, 19.8, 25.0, 31.2, 28.4, 18.0]
check_temperatures(temps)