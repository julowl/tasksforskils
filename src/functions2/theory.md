Functions — Theory (brief)

1. What is a function?
- A function is a reusable block of code that performs a specific task and can be called with arguments to produce a result.

2. Function signatures and annotations
- A function has a name, parameters, optional default values, and an optional return value. Use type annotations to document expected types: def f(x: int) -> int.

3. Positional, keyword, *args and **kwargs
- Positional arguments are matched by position. Keyword arguments by name. *args collects extra positional arguments as a tuple. **kwargs collects extra keyword arguments as a dict.

4. Higher-order functions
- Functions can accept other functions as arguments and can return functions. Examples: map, filter, sorted with key.

5. Closures
- A closure is a function that captures variables from its enclosing scope. Useful for encapsulating state (e.g., counters, memoization).

6. Decorators
- A decorator is a callable that transforms a function, often used to add behavior such as logging, caching, or validation. Implemented with @decorator syntax.

7. Recursion
- A function that calls itself. Useful for tree-like or nested structures. Always ensure a base case to avoid infinite recursion.

8. Lambda and functional tools
- lambda creates small anonymous functions. Combined with map, filter, and reduce they allow concise data transformations.

Tips
- Prefer clear readable code and use docstrings to document requirements. Use unit tests to validate behavior.
