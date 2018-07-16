import datetime

def function_print_next_day():
    tor=datetime.date.today()+datetime.timedelta(days=1)
    x=datetime.date.isoformat(tor)
    return x 


print(function_print_next_day())