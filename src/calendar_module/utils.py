import calendar
import logging
logging.basicConfig(level= logging.INFO , format= '%(message)s')
def calendar_module():
    m, d, y = map(int, input().split())
    weekday_date = calendar.weekday(y, m, d)
    weekday_name = calendar.day_name[weekday_date]
    logging.info(weekday_name.upper())
    return weekday_name.upper()
