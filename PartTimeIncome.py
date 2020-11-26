def main():
    """
    Gets necessary data from a user and calculates his net wage.
    At the end it prints a result.
    """
    student = isStudent()
    contract = contractType()
    discount = taxCredit()
    shift = hoursPerShift()
    days = workingDays()
    wage = hourWage()
    total = shift * days * wage
    tax = 0

    if contract == 'dpp' and total > 10_000:
        total = (total / 100) * 89
        tax = (total / 100) * 15

    elif contract == 'dpc' and total < 3_000:
        tax = (total / 100) * 15

    elif contract == 'dpc' and total > 3_000:
        total = (total / 100) * 89
        tax = (total / 100) * 15

    if tax and discount:
        tax -= 2070

    if tax and student:
        tax -= 370

    if tax > 0:
        total -= tax

    print(f'Your total income for this month is: {round(total)} CZK.')


def isStudent():
    """
    Asks the user if he study and checks a correct format.
    """
    while True:
        try:
            q = input('Are you student? y/n ')
            if q == 'y':
                return True
            elif q == 'n':
                return False
            else:
                raise ValueError

        except ValueError:
            print('Please enter "y" or "n".')
            continue

def contractType():
    """
    Asks the user for his contract type and checks a correct format.
    """
    cType = None
    while True:
        try:
            cType = input('What type of contract do you have? DPP/DPC ')
            cType = cType.lower()
            if cType == 'dpp' or cType == 'dpc':
                break
            else:
                raise ValueError

        except ValueError:
            print('Please enter "DPP" or "DPC".')
            continue

    return cType

def taxCredit():
    """
    Asks the user if he signed a tax credit and checks a correct format.
    """
    while True:
        try:
            tax = input('Have you signed tax credit (pink paper)? y/n ')
            if tax == 'y':
                return True
            elif tax == 'n':
                return False
            else:
                raise ValueError

        except ValueError:
            print('Please enter "y" or "n".')
            continue

def hoursPerShift():
    """
    Asks the user how long are his shifts and pauses and checks a correct format.
    """
    hours = None
    while True:
        try:
            hours = float(input('How long in hours is your shift? '))
            if hours < 1 or hours > 24:
                raise ValueError

            pauses = float(input('How long in total in minutes are pauses if '
                               'any? ' ))
            if pauses < 0 or pauses > hours * 60:
                raise ValueError

            if pauses:
                hours -= pauses / 60

            break

        except ValueError:
            print('Please enter correct number of hours and pauses.')
            continue

    return hours


def workingDays():
    """
    Asks the user how many days he plans to work and checks a correct format.
    """
     num = None
     while True:
        try:
            num = int(input('How many days a month have you worked or plan '
                            'to work? '))
            if num < 1 or num > 31:
                raise ValueError
            else:
                break

        except ValueError:
            print('Please enter a correct number of days.')
            continue

     return num

def hourWage():
    """
    Asks user what's his hour wage and checks a correct format.
    """
    wage = None
    while True:
        try:
            wage = int(input('What\'s your hour wage? '))
            if wage < 1:
                raise ValueError
            else:
                break

        except ValueError:
            print('Please enter correct hour wage.')
            continue

    return wage

main()
