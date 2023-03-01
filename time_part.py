import datetime
date = datetime.datetime.now()

#вывод сколько времени
hour_min = date.strftime('%H_%M')

#вывод даты https://highload.today/modul-datetime-v-python/
year_month_day = date.strftime('%d.%m.20%y')

print(year_month_day)
