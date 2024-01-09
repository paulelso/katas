from datetime import datetime

def most_weekend_birthdays(friends, conversation_date):
    conversation_date = datetime.strptime(conversation_date, "%Y-%m-%d")
    friend_counts = {}

    for friend, birth_date in friends:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        count = 0

        for year in range(birth_date.year, conversation_date.year + 1):
            if datetime(year, birth_date.month, birth_date.day).weekday() in [5, 6]:
                count += 1

        friend_counts[friend] = count

    max_count = max(friend_counts.values())
    youngest_friends = [friend for friend, count in friend_counts.items() if count == max_count]
    youngest_friends.sort(key=lambda x: datetime.strptime(friends[x], "%Y-%m-%d"))

    return youngest_friends[0]
