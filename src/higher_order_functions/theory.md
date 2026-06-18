Higher-order functions (HOFs) in Python

Overview (3-minute read):

Higher-order functions are functions that either take other functions as arguments, return functions as results, or both. They are a fundamental concept in functional programming and allow for concise, expressive, and reusable code.

Common patterns:

- Functions as arguments: You can pass functions to other functions to control behavior. Examples: map, filter, sorted(key=...), reduce (functools.reduce).
- Functions as return values: Functions can create and return other functions (closures). This enables building factories, partial application, and custom decorators.
- Composition and combinators: Building new functions by combining existing ones (e.g., composing f and g to create f(g(x))).

Key benefits:

- Abstraction: Move variable behavior into functions so you can reuse algorithmic structure.
- Reusability: Small functions composed together reduce duplication.
- Readability: Express intent (filtering, mapping, reducing) concisely.

Pitfalls and tips:

- Be explicit about side effects: Pure functions (no side effects) are easier to reason about and test.
- Prefer small, focused functions: Easier to test and combine.
- Use type hints: They help document expected function signatures (e.g., Callable[[int], bool]).

This exercise set covers:

- Receiving user-provided predicate/filter functions and applying them.
- Receiving user-provided aggregation functions and using them.
- Creating functions that return filters or aggregators.
- Combining filters and aggregators into pipelines.
- Verifying correctness with unit tests and doctests.

How to use these exercises:

Each Python file contains three exercises. Implement the functions marked with NotImplementedError. Run the unit tests at the bottom of each file to verify correctness. Read the docstrings for requirements and example pydoc tests.

Further reading:

- functools module (partial, reduce, wraps)
- typing.Callable for type annotations
- itertools for advanced composition patterns
