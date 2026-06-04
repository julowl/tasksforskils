Classes in Python — Short Theory (3-minute read)

1. What is a class?
- A class is a blueprint for creating objects (instances). Classes group data (attributes) and behavior (methods) together.

2. Instance vs Class attributes
- Instance attributes are stored on each instance (self.x). Class attributes are shared across all instances (MyClass.count).

3. Methods and the self parameter
- Instance methods receive the instance as the first parameter (conventionally named self). Class methods receive the class (cls) and are decorated with @classmethod. Static methods don’t receive either automatically and are decorated with @staticmethod.

4. Inheritance and polymorphism
- A class can inherit from another to reuse or extend behavior. Subclasses can override methods and call the parent implementation with super(). Polymorphism lets code operate on objects of different classes through a common interface.

5. Special (magic) methods
- Python classes implement special behaviors via methods like __init__, __repr__, __str__, __eq__, __add__, __len__, etc. These let objects work with built-in operations.

6. Properties and descriptors
- Use @property to expose computed attributes with getter/setter/deleter semantics. This provides attribute-like access while allowing validation or lazy computation.

7. Composition and Factory patterns
- Composition means building classes by holding references to other objects rather than inheriting. Factory methods (often @classmethod) provide alternative constructors.

Why exercises?
- Implementing classes teaches design decisions: where to store state (class vs instance), when to override behavior, and how to make objects behave like built-ins. The exercises below focus on these nuances.

Read the exercises files in src/. Each exercise contains placeholders (raise NotImplemented) and tests. Fill the implementations and run them to validate.
