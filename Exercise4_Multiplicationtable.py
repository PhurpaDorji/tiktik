#Get the number for which the multiplication table is required
number = int(input("Enter the number for which you want the multiplication table: "))

#Get the limits up to which the multiplication table should be generated
limit = int(input("Enter the limits u to which the multiplication table be generated: "))

#Generate and print the multiplication table )
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * 1}")