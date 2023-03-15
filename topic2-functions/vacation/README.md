## Vacation

In this assignment, you will write a program to calculate the total cost of a hypothetical vacation.

### Description

You're going on vacation! But you need to know the cost of that vacation...

Your plan is to write a number of functions that help you calculate the total cost of a vacation. Here are the functions you'll need to write:

1. `hotelCost`
   - param {int}: `nights` - the number of nights you'll stay
   - param {float}: `nightlyRate` - the cost of the hotel per night
   - return {float}: the total cost of a stay at the hotel for the duration of your stay
2. `flightCost`
   - param {str}: `city` - the city in which you'll stay
   - return {float}: the total cost of flight from Philadelphia to the given city.
   - note: the function should have at least five cities and their associated costs; these should be hard-coded into the function
3. `rentalCarCost`
   - param {int}: `days` - the number of days you'll need the car
   - return {float}: the total cost renting the car
   - note: the algorithm for the cost of a rental car is as follows:
     - the base cost is $40 per day
     - if the car is rented for seven or more days, a one-time discount of $50 is applied
     - if the car is rented for three or more days, a one-time discount of $20 is applied
     - only one discount may be applied per rental
4. `totalCost`
   - param {int}: `days`- the number of days you're staying
   - param {int}: `nights` - the number of nights you're staying
   - param {float}: `hotelRate` - the nightly cost of the hotel
   - param {str}: `city` - the city to which you're travelling
   - return {float}: the total cost of the entire facation

Your program should also include a `main` function, which of course takes no parameters and does not return anything. `main` should inform the user of the purpose of the program and take user input for each of the four parameters of `totalCost`, using those inputs as arguments for the `totalCost`. The program should print the total to the user after calculation.

### Learning Targets

By the end of this assignment, you should be able to:

- Write a function that accomplishes a given task
- Differentiate between parameters and arguments
- Return correct values--and only correct values--from a function
- Test code for intended behavior and unforeseen errors
