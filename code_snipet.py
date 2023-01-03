import pandas as pd
import datetime

current_dates = ['02/06/1989', '04/12/1999', '05/03/1995']
new_dates = ['02/06/1989', '04/12/1999', '05/03/1995',
             '02/03/1989', '04/11/1999', '05/01/1995',
            '02/06/1999', '04/12/2009', '05/03/2015']

latest_date = max(map(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'), current_dates))
current_dates += filter(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y')>latest_date, new_dates)
current_dates

begin_date = '1999-10-16'
df_all = pd.DataFrame({'forecast_date':pd.date_range(begin_date, periods=3000)})
begin_date = '2019-10-27'
df2 = pd.DataFrame({'forecast_date':pd.date_range(latest_date, periods=300)})

df_new = pd.concat([df2, df_all[df_all['forecast_date'] > df2['forecast_date'].max()]])
