def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...
def calculate_weekly_pay(hours_worked, hourly_rate):
    if hours_worked <= 0 or hourly_rate <= 0:
        return 0  
    if hours_worked <= 40:
        weekly_pay = hours_worked * hourly_rate
    else:
        
        weekly_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        weekly_pay += overtime_pay
    return weekly_pay 
hours_worked = 45  
hourly_rate = 15   
pay = calculate_weekly_pay(hours_worked, hourly_rate)
print(f"The weekly pay is: £{pay:.2f}")


    
# # Code Example
# overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
# print(overtime_pay)
