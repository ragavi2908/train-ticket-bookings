print("Welcome to Indian Railways")

gender_select = input("What gender you are: ")
gender = ("1.female", "2.male")
print("2.male" in gender) 

destination = {"trichy": 200, "madurai": 350, "chennai": 450, "thirunelveli": 500}

your_dest = input("Enter your destination: ").lower()
if your_dest in destination:
    print(f'Ticket for your {your_dest.title()} is available')
    
    your_class = input("Enter your class (AC / sleeper / normal): ").lower()
    ticket = int(input("How many tickets you want: "))
    base_price = destination[your_dest] * ticket

    if your_class == "ac" or your_class == "sleeper":
        gst_price = base_price * 12 / 100
    elif your_class == "normal":
        gst_price = base_price * 5 / 100
    else:
        print("Invalid class selected.")
        exit()

    total_price = gst_price + base_price
    print(f"\nYour total price for your journey to {your_dest.title()} is ₹{total_price:.2f} with GST applied.")

else:
    print("Sorry, tickets not available.")
