# #Calender creation
# import calendar

# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year, month)
# print(cal)

#creating a calender that takes in the year,month and day for an investment
import calendar
name = input("Name: ")
money = input("Money invested: ")
interest_rate = input("Interest Rate (%): ")


class HighlightCalendar(calendar.TextCalendar): #highlight calendar takes all the attribute of the inbuilt calender in python(textcalendar)
    def __init__(self, highlight_day): #self makes reference to the instance of the class highlightcalender
        super().__init__() 
        self.highlight_day = highlight_day

    def formatday(self, day, weekday, width): #it highlight the specific day been referenced and lives other unhighlighted
        if day == self.highlight_day:
            return f'[{day:2d}]'
        else:
            return super().formatday(day, weekday, width) 

highlight_day = int(input("Enter checkout day: "))
month = int(input("Enter the month: "))
cal = HighlightCalendar(highlight_day)

money = float(money)

interest_rate = float(interest_rate) *.01 
n = int(input("Duration: "))
for i in range (n):
    money = money + (money * interest_rate)
    
print(f"Hi {name}, your ROI after 3 weeks is {money :.2f} Naira only, for the date in the calendar below.")
cal.prmonth(2024, month)
