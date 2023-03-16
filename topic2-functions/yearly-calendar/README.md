## Yearly Calendar

In this assignment, you will use your `printMonthCalendar` function to write a program that prints the calendar for a whole year.

### Description

Write a program that prints an aligned yearly calendar, with the correct number of days in each month. You will not be using the actual Gregorian calendar dates for the year provided. Instead, your yearly calendar function will take as input the day of the week of January 1st, and print the calendar based on that information.

The functions needed are listed below:

1. `printMonthCalendar`
   - param {int}: `numDays` - the number of days in the month
   - param {int}: `startDay` - an integer corresponding to the day of the week of the first day of the month; since calendars are most often printed with Sunday as the leftmost day of the week, allow 0 to correspond to Sunday
   - return {int}: an integer corresponding to the day of the week of the last day of the month
   - note: the return value is only part of this function's role; it must also print an aligned monthly calendar
2. `isLeapYear`
   - param {int}: `year` - the year in question
   - return {bool}: - True if the year is a leap year; False if not
   - note: the algorithm for determining a leap year is as follows:
     - a year is a leap year if it is divisible by 4 but not by 100
     - if a year is divisible by 400, then it is also a leap year
     - examples:
       - 1996 _is_ a leap year (divisible by 4)
       - 2000 _is_ a leap year (divisible by 400)
       - 1900 _is not_ a leap year (divisible by 4 and 100 but not 400)
3. `printYearCalendar`
   - param {int}: `year` - the year in question
   - param {int}: `startDay` - an integer corresponding to the day of the week of January 1st; since calendars are most often printed with Sunday as the leftmost day of the week, allow 0 to correspond to Sunday
   - return {int}: an integer corresponding to the day of the week of December 31st
   - note: the return value is only part of this function's role; it must also print the aligned yearly calendar

Your program should also include a `main` function, which of course takes no parameters and does not return anything. `main` should prompt the user for the year and the integer corrresponding the day of January 1st. It will be wise to carefully consider how you ask the user for the day of the week, as they won't necessarily understand the encoding of the days with integers 0-6. Though it may be obvious at this point, `main` should also call `printYearCalendar`.

<img src="" alt="" width="600" height="295">

### Learning Targets

By the end of this assignment, you should be able to:

- Compose multiple user-defined functions to complete a task
- Coordinate return values between multiple composed functions
- Write a main function that utilizes (either directly or indirectly) all other user-defined functions in the program
- Apply the logic and rules of modular arithmetic to determine whether a year is a leap year
- Decompose a large task into smaller sub-tasks, writing a function to accomplsih each sub-task
