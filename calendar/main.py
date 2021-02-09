import calendar

calendar.setfirstweekday(0)
# Ustawienie który dzień ma być pierwszym 1 -> Monday, 6 -> Sunday

year = 2021
month = 1
spacingx = 1
# odstępy między tygodniami
spacingy = 2
# odstępy między miesiącami

print(calendar.month(year, month))

print("#######################")

print(calendar.calendar(year, month, spacingx, spacingy))

# HTML

calendarinio = calendar.HTMLCalendar().formatmonth(year, month)

# ###

file = open("./calendar/index.html", "w")

file.write(f"{calendarinio}")

file.close()
