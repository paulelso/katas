# Weekend Birthdays

https://www.codewars.com/kata/6375e9030ac764004a036840/train/python

# Introduction
Not having to go to school or work on your birthday is always a treat, so when your birthday would have fallen on a weekend, it's really annoying if a leap year means you miss out. Some friends are discussing this and think they have missed out more than others, so they need your help.

T#he Challenge
Given a list of friends, their dates of birth and the date of their conversation, work out who has had the most birthdays fall on a Saturday or Sunday up to and including the date of the conversation. If more than one friend shares that number of weekend birthdays, return the youngest. If the youngest shares their birthday with other friends, then any of the youngest will be accepted.

When counting weekend days, don't include the day on which they were born - after all, they wouldn't have been familiar with the concept of a weekend right then! Friends born on 29th February celebrate their birthdays on 28th February in non-leap years.

# Example
The friends are provided as a sequence of pairs containing their name and their date of birth in the format YYYY-MM-DD. The date of their conversation is provided in the similar format.

most_weekend_birthdays([("Alice", "2010-11-10"), ("Bob", "2010-11-23")], "2022-12-31") ==> "Alice"
Alice has four birthdays falling on a weekend (Saturday in 2012 and 2018, Sunday in 2013 and 2019) compared to three for Bob (Saturday in 2013 and 2019, Sunday in 2014).

