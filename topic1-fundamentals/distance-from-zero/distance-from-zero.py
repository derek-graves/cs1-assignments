"""
This is a fairly straightforward assignment meant to give
students first practice writing a funtion and handling
return values. Student work sould look something like this.
"""

def distanceFromZero(value):
    if isinstance(value, int) or isinstance(value, float):
        return abs(value)
    else:
        return "You have entered an invalid data type. Please use a number."
    
print(distanceFromZero(-4.5))
print(distanceFromZero("Testing...1, 2, 3...testing"))
print(distanceFromZero(True))


"""
Note that if students use a boolean as their invalid test
value, they'll likely get 0 (False) or 1 (True). If
students are interested, feel free to introduce them to
the idea of 'truthy' and 'falsey' values.
"""