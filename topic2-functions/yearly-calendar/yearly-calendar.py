"""
As with many Computer Science assignments, there are
numerous ways that students can accopmlsih the given task.
Student code should look something like the program below,
and student output should like very similar to the output
produced by this solution.
"""


def printWeekDays():
  print("Sun", end="   ")
  print("Mon", end="   ")
  print("Tue", end="   ")
  print("Wed", end="   ")
  print("Thu", end="   ")
  print("Fri", end="   ")
  print("Sat", end="   ")
  print("\n")

"""
printWeekDays is not a necessary function, but it produces
a cleaner-looking printMonthCalendar function
"""

def printMonthCalendar(numDays, startDay):
  # print days of the week as column headers
  printWeekDays()

  # create whitespace in first line based on startDay
  for i in range(startDay):
    print("", end="      ")
  
  currentDay = startDay
  for i in range(1, numDays + 1):
    # print day number and requisite number of spaces/tabs
    if i >= 10:
      endString = "    "
    else:
      endString = "     "
    print(i, end=endString)  
    
    # go to new line if currentDay is a Saturday and not the end of the month
    currentDay += 1
    if currentDay > 6:
      currentDay = 0
      print("\n")

  print("\n")
  return currentDay - 1

def isLeapYear(year):
  output = False
  if (year % 400) == 0 or (((year % 4) == 0) and ((year % 100) != 0)):
    output = True

  return output

def printYearCalendar(year, startDay):
  febDays = 28
  if isLeapYear(year):
    febDays = 29

  endDayTracker = startDay
  
  print("January", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  print("February", year)
  endDayTracker = printMonthCalendar(febDays, endDayTracker) + 1

  print("March", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  print("April", year)
  endDayTracker = printMonthCalendar(30, endDayTracker) + 1

  print("May", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  print("June", year)
  endDayTracker = printMonthCalendar(30, endDayTracker) + 1

  print("July", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  print("August", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  print("September", year)
  endDayTracker = printMonthCalendar(30, endDayTracker) + 1

  print("October", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  print("November", year)
  endDayTracker = printMonthCalendar(30, endDayTracker) + 1

  print("December", year)
  endDayTracker = printMonthCalendar(31, endDayTracker) + 1

  return endDayTracker - 1

def main():
  print("\n")
  userYear = int(input("What is your desired year? "))
  yearStartDay = int(input("Using the guide below, please enter the number corresponding to the day of the week of January 1st:\n0 = Sunday\n1 = Monday\n2 = Tuesday\n3 = Wednesday\n4 = Thursday\n5 = Friday\n6 = Saturday\n\nStart day: "))
  print("\n")
  
  printYearCalendar(userYear, yearStartDay)


main()