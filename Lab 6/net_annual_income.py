# def annual_net_income(gross_salary):
    # complete your function implementation here...
def annual_net_income(gross_salary):
    tax_rate = 0.20 
    tax_amount = gross_salary * tax_rate
    net_income = gross_salary - tax_amount
    return net_income
gross_salary = 50000
net_income = annual_net_income(gross_salary)
print(f"The annual net income for a gross salary of £{gross_salary} is £{net_income}")

    #return net_salary
        




