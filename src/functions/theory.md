Python Functions — Theory (short)

This short guide (≈3 minutes) covers the essential concepts about Python functions needed for the exercises.

1. What is a function?
- A function is a named block of reusable code that can accept inputs (parameters) and return an output.
- Defined with def name(params): and a return statement.

2. Parameters and arguments
- Positional parameters: def foo(a, b)
- Default parameters: def foo(a, b=2)
- Variable positional args: *args (tuple of extra positional arguments)
- Variable keyword args: **kwargs (dict of extra named arguments)

3. Return values
- Functions can return single values, tuples, lists, dicts, or None.
- Use return to exit and give back a value.

4. First-class functions
- Functions are objects: they can be assigned to variables, passed as arguments, and returned from other functions.
- Higher-order functions either take or return functions.

5. Closures
- A closure is a function that retains access to variables from its defining scope even after that scope has finished execution.
- Useful for creating parameterized functions (e.g., make_multiplier).

6. Recursion
- A function can call itself to solve smaller subproblems.
- Always ensure a base case to prevent infinite recursion.

7. Decorators
- A decorator is a function that takes a function and returns a modified function.
- Commonly used for caching, logging, access control, retries, etc.

Tips for the exercises
- Read the docstrings for each exercise function — they explain what to implement.
- Run tests with pytest (install pytest if needed).
- Keep implementations small and test-driven: run tests often.

That's it — now try the hands-on exercises in the same folder.