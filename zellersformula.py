def zellers_formula(day, month, year):
    
    d = year % 100
    c = year // 100
    
    day_of_week = (day + ((13 * (month + 1)) // 5) + d + (d // 4) + (c // 4) - (2 * c)) 
    # Convert to 0 for Saturday, 1 for Sunday, ..., 6 for Friday
    return (day_of_week + 5) % 7

# Example usage
day = 19
month = 4
year = 2024
day_of_week = zellers_formula(day, month, year)
days_of_week = ["saturday","sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"The day of the week for {day}/{month}/{year} is {days_of_week[day_of_week]}.")
