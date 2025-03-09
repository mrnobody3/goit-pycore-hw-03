from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int:
    try:
        given_date = dtdt.strptime(date, "%Y-%m-%d").date()
        today_date = dtdt.today().date()
        print('today_date:', today_date)
        return (today_date - given_date).days
    except ValueError:
        raise ValueError("Date format is wrong, use 'yyyy-mm-dd'.")

print(get_days_from_today("2021-10-09"))