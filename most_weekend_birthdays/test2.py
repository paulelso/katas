from datetime import datetime, timedelta

def main():
    s = [("Alice", "2010-11-10"), ("Bob", "2010-11-23")], "2022-12-31"
    friends, conversation_date = s
    print(most_weekend_birthdays(friends, conversation_date))

def most_weekend_birthdays(friends, conversation_date):
    # Convert conversation_date to datetime object
    conversation_date = datetime.strptime(conversation_date, "%Y-%m-%d")
    
    # Initialize variables to keep track of the friend with the most weekend birthdays
    max_weekend_birthdays = 0
    youngest_friend = None
    
    for friend, dob in friends:
        print(friend, dob)
        # Convert dob to datetime object
        dob = datetime.strptime(dob, "%Y-%m-%d")
        
        # Initialize variables to count weekend birthdays
        weekend_birthdays = 0
        current_date = dob + timedelta(days=1)  # Start from the day after the friend's birthday
        
        while current_date <= conversation_date:
            # Check if the current date is a Saturday or Sunday
            if current_date.weekday() in [5, 6]:
                weekend_birthdays += 1
            
            # Increment current_date by 1 year
            current_date = current_date.replace(year=current_date.year + 1)
        
        # Update max_weekend_birthdays and youngest_friend if necessary
        if weekend_birthdays > max_weekend_birthdays:
            max_weekend_birthdays = weekend_birthdays
            max_name = friend
        elif weekend_birthdays == max_weekend_birthdays:
            # Compare the ages of the friends
            if dob > datetime.strptime(friends[youngest_friend], "%Y-%m-%d"):
                max_name = friend

        print(f"{friend}: {weekend_birthdays}")
    
    return max_name

if __name__ == "__main__":
    main()
