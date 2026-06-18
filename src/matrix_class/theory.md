Execution plan

1) Plan and subtopics
- Basic Matrix representation and validation: construction, rectangular check, shape, is_square.
- Matrix creation helpers: zeros, identity, from_list and to_list conversions.
- Indexing and mutation: __getitem__, __setitem__, row and column accessors.
- Arithmetic operations: element-wise addition, subtraction, scalar multiplication and operators.
- Multiplication: matrix multiplication (matmul), multiply by vector, Hadamard product.
- Advanced operations: transpose, trace and determinant (recursive expansion).
- Utilities: exact equality, approximate equality with tolerance, safe deep-copy conversion.

2) List of 7 source files
- matrix_basic.py
- matrix_creation.py
- matrix_indexing.py
- matrix_arithmetic.py
- matrix_multiplication.py
- matrix_advanced.py
- matrix_utils.py

3) Short review
These exercises convert procedural matrix utilities into class-based tasks. Each source file contains three focused exercises implemented as methods or classmethods of a Matrix class. Students will practice API design with classes, defensive validation, operator overloading, and numerical considerations (tolerances). Tests are provided to guide behavior and edge cases.

Theory (3 minutes read)

Why classes for matrices?
- Encapsulation: a Matrix class groups data and behavior (validation, arithmetic, transforms) in one place.
- Reuse: methods like transpose or multiplication operate naturally on instances.
- Operators: Python provides magic methods (like __add__, __matmul__) which make code clearer and more idiomatic.

Representing matrices
- A simple and common internal representation is a nested list: List[List[float]].
- Ensure rectangular shape: all rows must have the same number of columns. Empty matrix can be represented as an empty list [].
- Use deep copies when exposing or storing data to prevent accidental external mutation.

Basic operations
- shape: return (rows, cols). For [], shape is (0,0).
- is_square: True when rows == cols and rows > 0.
- zeros and identity: classmethods that construct matrices without requiring users to pass raw lists.

Indexing and mutation
- __getitem__ can be flexible: m[i] returns the i-th row, m[i,j] returns a specific element.
- __setitem__ should support element assignment for m[i,j] = value.
- Provide convenience row(r) and col(c) methods that return copied lists.

Arithmetic
- Element-wise add/sub require same shapes; raise ValueError on mismatch.
- Scalar multiplication should create a new Matrix; implement __mul__ for convenience.
- Don't mutate original operands unless explicitly documented.

Multiplication
- Matrix multiplication (A @ B) is defined when A.cols == B.rows.
- Multiplying by a vector returns a list of floats representing the resulting column.
- Hadamard product multiplies corresponding elements and requires identical shapes.

Advanced operations
- transpose flips rows and columns. Empty matrix transpose is empty.
- trace sums diagonal elements — only for square matrices.
- determinant can be implemented recursively using expansion by minors (ok for small matrices used in exercises).

Equality and tolerances
- Exact equality compares shapes and exact float values.
- Approximate equality compares floats within a tolerance. Useful when working with floating point arithmetic.

How to use the exercises
- Each source file contains stubbed methods raising NotImplementedError.
- Implement methods to satisfy the provided doctests and the unittest suite at the bottom of each file.
- Run pytest or python file to run the unit tests and iteratively implement missing pieces.
