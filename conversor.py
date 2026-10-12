def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print("--- Conversor de Temperatura ---")
    try:
        c = float(input("Introduce los grados Celsius: "))
        f = celsius_a_fahrenheit(c)
        print(f"{c}°C equivalen a {f:.2f}°F")
    except ValueError:
        print("Por favor, introduce un número válido.")