## Distance From Zero

In this assignment, you will write a function that returns to absolute value of a number.

### Description

Write a function called `distanceFromZero` that takes one parameter. If the type of the parameter is `int` or `float`, return the absolute value of the input. Otherwise, return a string indicating to the user that they used the wrong input. For the absolute value portion, feel free to use Python's built in `abs` function.

You will likely need the `isinstance` function that is built into Python. This function takes two parameters, an object and a datatype, and returns a boolean indicating whether the object was of the given type. For example, the following call to the function would evaluate to False, because x is not a string.

```
x = 6
isinstance(x, str)
```

After your function, write some code that shows at least one example of the function returning the absolute value of the argument, and at least one example of the function telling the user they included the wrong input. Sample output is included below.

<img src="./times-table-example.jpg" alt="Times Table Sample" width="600" height="330">

### Learning Targets

By the end of this assignment, you should be able to:

- Write a function that accomplishes a given task
- Differentiate between parameters and arguments
- Return correct values--and only correct values--from a function
- Test code for intended behavior and unforeseen errors
