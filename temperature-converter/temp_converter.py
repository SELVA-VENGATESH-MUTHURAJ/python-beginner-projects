print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose (1/2): ")

if choice == "1":
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print(f"Fahrenheit: {f:.2f}")

elif choice == "2":
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Celsius: {c:.2f}")

else:
    print("Invalid choice.")
