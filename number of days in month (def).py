#Number of days per month. First value placeholder for indexing purposes.
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap(year):
    """return true for leap years, Flase for non-leap years"""
    return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year, month):
    """ return number of days in that month in that year."""
    if not 1<= month <=12:
        return 'invalid month'
    if month==2 and leap(year):
        return 29
    return month_days[month]
month=int(input('number of month: '))
year=int(input('which year: '))
print('number of day is:',days_in_month(year,month))
