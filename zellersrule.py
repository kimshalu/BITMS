def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_valid_date(day, month, year):
    if year < 1900 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if month == 2:
        if is_leap_year(year):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 31:
            return False
    return True
    

def zellers_formula(day, month, year):
    
    d = year % 100
    c = year // 100
    # Zeller's  formula
    day_of_week = (day + ((13 * (month - 1)) // 5) + d + (d // 4) + (c // 4) - (2 * c)) 
    return (day_of_week+1) % 7

def zellers_with_leap(year):
    day = 1
    month = 2
    if is_leap_year(year):
        return zellers_formula(day, month, year)
    else:
        
        return zellers_formula(day, month-1, year)

day = int(input('enter the day:'))
month =int(input('enter month:'))
year = int(input('enter year:'))

if is_valid_date(day, month, year):
    day_of_week = zellers_with_leap(year)
    days_of_week = { 0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday",6:"Saturday"}
    print(f"The {day}-day of the week for {month}th month, {year} is {days_of_week[day_of_week]}.")
else:
    print("Invalid date entered.")
