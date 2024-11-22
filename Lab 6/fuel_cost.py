# def fuel_cost(distance_miles):
#     # Constants
#     MPG = 50  # Miles per gallon
#     LITERS_PER_GALLON = 4.5
#     PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
def fuel_cost(distance_miles):
    # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  
    gallons_needed = distance_miles / MPG
    liters_needed = gallons_needed * LITERS_PER_GALLON
    cost = liters_needed * PRICE_PER_LITER
    return cost
distance = 100  # miles
cost = fuel_cost(distance)
print(f"The fuel cost for {distance} miles is £{cost:.2f}.")

    # return total_cost

