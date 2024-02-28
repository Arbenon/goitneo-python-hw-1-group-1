from datetime import datetime, timedelta
from collections import defaultdict


def get_birthday_per_week(users):
    present_date = datetime.now()
    day_name_bd = defaultdict(list)
    formatted_birthdays = ''

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=present_date.year)
   
        day_name = 'Later'


        if birthday_this_year > present_date.date():
            delta_days = (birthday_this_year - present_date.date())
            if delta_days < timedelta(days=7):
                day_name = birthday_this_year.strftime("%A")
                if day_name == 'Saturday':
                    birthday_this_year += timedelta(days=2)

                elif day_name == 'Sunday':
                    birthday_this_year += timedelta(days=1)
                day_name = birthday_this_year.strftime("%A")
                day_name_bd[day_name].append(name)

    for day, name in day_name_bd.items():
        formatted_birthdays += "".join([f"{day}: {', '.join(name)} \n"])
    formatted_birthdays = formatted_birthdays.rstrip('\n')
    
    return formatted_birthdays

