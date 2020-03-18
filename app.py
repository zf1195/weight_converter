weight = int(input("Weight: "))
pounds_or_kilograms = input("(L)bs or (K)g: ")

if pounds_or_kilograms.upper() == "L":
    converted_measurement = weight * 0.45
    print(f"You are {converted_measurement} kilograms")
elif pounds_or_kilograms.upper() == "K":
    converted_measurement = weight * 2.20
    print(f"You are {converted_measurement} pounds")
else:
    print("Enter valid response")
