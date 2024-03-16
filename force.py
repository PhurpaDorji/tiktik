print("Newton second law of motion")
print("....................................")

#Determine the missing value
print("select the missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (f)")
missing_value_choice = input("Enter the option number for the missing value: ")

#prompt the user to enter the other tow values
if missing_value_choice  =="1":
    a = float(input("Enter acceleration (a): "))
    f = float(input("Enter force (F) : "))
    m = F / a
    print(f"msaa (m) = {m}")

    elif missing_value_choice =="2"
    m = float(input("Enter mass (m): "))
    F = float(input("Enter force (f): "))
    a = F / m
    print(f"Acceleration (a) = {a}")

    elif missing_value_choice == "3":
        m = float(input("Enter mass (m): "))
        a = float(input("Enter acceleration (a): "))
        F = m * a
        print(f"Force (f) = {F}")

        else:
            print("Invalid option selectrd for the missing value.")
