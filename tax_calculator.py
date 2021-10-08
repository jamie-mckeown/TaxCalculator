thresholds = {
    "national insurance"    :   (0.12, 184.0)  ,  #   £184 per week.
    "income tax"            :   (0.2, 12570.0)     #  £12500 a year as given on the government website.
}

def calculate_income_tax (wage:float) :
    '''Takes an untaxed wage (assumed 4-weekly) and returns the income tax paid on this wage.'''
    percentage, threshold = thresholds["income tax"]
    threshold = threshold/13.0 # scale up to 4-weeks

    if wage > threshold :
        taxable = wage - threshold
        return taxable*percentage
    else:
        return 0.0

def calculate_national_insurance (wage:float) :
    '''Takes an untaxed wage (assumed 4-weekly) and returns the national insurance paid on this wage.'''
    percentage, threshold = thresholds["national insurance"]
    threshold = threshold*4.0 # scale up to 4-weekly

    if wage > threshold :
        taxable = wage - threshold
        return taxable*percentage
    else:
        return 0.0

def calculate_take_home (wage:float) :
    '''Takes a 4-weekly wage and returns the take-home pay after National Insurance and Income Tax contributions.'''

    income_tax = calculate_income_tax(wage)
    national_insurance = calculate_national_insurance(wage)
    
    tax_paid = income_tax + national_insurance

    take_home = wage - tax_paid

    return round(take_home,2)


######  RUN PROGRAM ######

I = input("Enter 4-weekly wage: ")

I = float(I)

take = round(calculate_take_home(I), 2)
ni = round(calculate_national_insurance(I), 2)
it = round(calculate_income_tax(I), 2)

if ni == 0.0 :
    ni = "0.00"

if it == 0.0 :
    it = "0.00"

result = f"Your take-home pay is £{take}. You will pay £{ni} National Insurance and £{it} Income Tax."


print(result)