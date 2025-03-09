from datetime import datetime as dtdt, timedelta as td

def get_upcoming_birthdays(users):
  
    today = dtdt.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_diff = (birthday_this_year - today).days
        if 0 <= days_diff <= 7:
            if birthday_this_year.weekday() in [5, 6]:  # Субота або неділя
                birthday_this_year += td(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
