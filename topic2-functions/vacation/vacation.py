def hotelCost(nights, nightlyRate):
    return nights * nightlyRate

def flightCost(city):
    if city == "New York":
        cost = 110.00
    elif city == "Boston":
        cost = 140.00
    elif city == "Los Angeles":
        cost = 550.00
    elif city == "Seattle":
        cost = 530.00
    elif city == "London":
        cost = 1000.00
    # students don't need to include an else case,
    # but it's good practice when writing branching statements
    else:
        cost = 10000.00
    
    return cost

def rentalCarCost(days):
    discount = 0
    if days >= 7:
        discount = 50.00
    elif days >= 3:
        discount = 20.00
    
    total = (40.00 * days) - discount
    return total

def totalCost(days, nights, hotelRate, city):
    total = hotelCost(nights, hotelRate) + flightCost(city) + rentalCarCost(days)
    return total

def main():
    print("\nWelcome to the vacation cost calculator!\n")
    destination = input("Where are you headed?\n")
    dayDuration = int(input("\nHow many days will you be gone?\n"))
    nightDuration = int(input("\nHow many nights are you staying?\n"))
    hotel = float(input("\nWhat's the nightly rate of the hotel where you're lodging?\n"))

    total = totalCost(dayDuration, nightDuration, hotel, destination)
    print("\nThe total cost of your vacation is $%.2f\n"%(total))


main()