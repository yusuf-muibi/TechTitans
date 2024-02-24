import calendar
name = input("Name: ")
money = input("Money invested: ")
interest_rate = input("Interest Rate (%): ")

class HighlightCalendar(calendar.TextCalendar):
    def __init__(self, highlight_day):
        super().__