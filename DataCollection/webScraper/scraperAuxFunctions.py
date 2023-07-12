

def divide_with_remainder(number, divider):
    quotient = number // divider  # Integer division
    remainder = number % divider  # Modulo operator

    return quotient, remainder


def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_days_in_month(year, month):
    """Get the number of days in a given month."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def increment_date(date):
    """Increment the date to the next day."""
    day, month, year = map(int, date.split('/'))
    days_in_month = get_days_in_month(year, month)

    if day < days_in_month:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1

    return day, month, year

def split_date_with_slash(day, month, year):
    return f"{day:02d}/{month:02d}/{year}"