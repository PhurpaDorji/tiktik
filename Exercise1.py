a=int(input("Please enter your age:\n "))
b=input(" Are you student? (yes or no)\n").lower()

if b=="yes":
    if (a <=18 and a>=13):
        print("You will get discount for your movie ticket")

    else:
        print("Sorry! We can't help you as your age exceed the ticket discount criteria")

else:
    print("You must bye the ticket without discount")