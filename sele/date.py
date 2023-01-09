import datetime
from datetime import date

def get_quarter(date):
    quarter = (date.month - 1) // 3 + 1
    return quarter

def get_quarter_dates(year, quarter):
    if quarter == 1:
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 3, 31)
    elif quarter == 2:
        start_date = datetime.date(year, 4, 1)
        end_date = datetime.date(year, 6, 30)
    elif quarter == 3:
        start_date = datetime.date(year, 7, 1)
        end_date = datetime.date(year, 9, 30)
    elif quarter == 4:
        start_date = datetime.date(year, 10, 1)
        end_date = datetime.date(year, 12, 31)
    else:
        start_date = None
        end_date = None
    return (start_date, end_date)






today = date.today()
target = today - datetime.timedelta(days=80)
year = target.year
quarter= get_quarter(target)

start_date, end_date = get_quarter_dates(year = year, quarter =  quarter)
print(f"Quarter {quarter} {year}: {start_date} - {end_date}")


start_date = datetime.datetime.strptime('13.01.2020', '%d.%m.%Y')
end_date = datetime.datetime.strptime('13.02.2020', '%d.%m.%Y')
i = 0
days = []
while True:
    target = start_date + datetime.timedelta(days=i)
    if target> end_date:
        break
    days += [target]
    i += 1


str_dates = list(map(lambda x: datetime.datetime.strftime(x, '%d/%m/%Y'), days))