def is_leap_year(year):
    """ determines if a year is a leap year

    returns a boolean """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0