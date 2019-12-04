import datetime


def add_month(my_date):
    if my_date.month ==12:
        new_date = datetime.date(year = my_date.year + 1, month=1, day=1)
    else:
        new_date = datetime.date(year = my_date.year, month=my_date.month + 1, day=1)
    
    return new_date

def reduce_month(my_date):
    if my_date.month ==1:
        new_date = datetime.date(year = my_date.year - 1, month=12, day=1)
    else:
        new_date = datetime.date(year = my_date.year, month=my_date.month - 1, day=1)
    
    return new_date
    