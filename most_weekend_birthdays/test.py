import calendar
from datetime import datetime
from datetime import datetime

def main():
    #s = ([("Alice", "2010-11-10"), ("Bob", "2010-11-23")], "2022-12-31")
    #s = ([("Steve", "2010-11-18"), ("Dave", "2010-11-22")], "2022-12-31")
    #s = [('Urma', '2002-03-06'), ('Victor', '2002-03-06'), ('Xavier', '2004-03-01')] , '2022-12-31'
    s = [("Ian", " "), ("Jane", "2022-12-31")]
    dobs, convo_dt = s
    print(most_weekend_birthdays(dobs, convo_dt))

def most_weekend_birthdays(dobs, convo_dt):
    try:
        convo_dt_obj = datetime.strptime(convo_dt, "%Y-%m-%d").date()
    except TypeError:
        exit(1)
    max_count = 0
    max_name = ""
    max_age = float('inf')  # Initialize with infinity
    for dob in dobs:
        count = 0
        name, dob = dob
        dob_dt_obj = datetime.strptime(dob, "%Y-%m-%d").date()        
        for i in range(dob_dt_obj.year + 1, convo_dt_obj.year):
            y, m, d = i, dob_dt_obj.month, dob_dt_obj.day
            if is_weekend(y, m, d):
                count += 1
        if count > max_count or (count == max_count and dob_dt_obj > max_age):
            max_count = count
            max_name = name
            max_age = dob_dt_obj
        print(f"{name}: {count}")
    return max_name

def is_weekend(year, month, day):
    weekday = calendar.weekday(year, month, day)
    if weekday == 5 or weekday == 6:
        return True

if __name__ == "__main__":
    main()