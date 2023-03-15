## Distance From Zero

In this assignment, you will write a function that returns to absolute value of a number.

### Description

Write a function called `distanceFromZero` that takes one parameter. If the type of the parameter is `int` or `float`, return the absolute value of the input. Otherwise, return a string indicating to the user that they used the wrong input.

You will likely need the `isinstance` function that is built into Python. This function takes two parameters, an object and a datatype, and returns a boolean indicating whether the object was of the given type. For example, the following call to the function would evaluate to False, because x is not a string.

```
x = 6
isinstance(x, str)
```

After your function, write some code that shows at least one example of the function returning the absolute value of the argument, and at least one example of the function telling the user they included the wrong input. Sample output is included below.

<img src="./times-table-example.jpg" alt="Times Table Sample" width="600" height="330">

### Learning Targets

By the end of this assignment, you should be able to:

- Evaluate and choose a loop structure based on whether it is well suited to the assigned task.
- Reuse a single block of code multiple times to solve a problem or complete a task.
- Create customized `print()` statements using the keyword argument `end`.
- Properly align text in the console by dynamically allocating and printing the correct number of spaces.
