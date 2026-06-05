---
name: Task creation
alwaysApply: true
description: Use this rule if you need to create a new task/exercises etc. For example if the user asks to create a task on the topic of "Typing" use this rule
---

# Task creation — Rule

Purpose
- For the topic of {TOPIC} create 7 exercises that highlight different approaches and nuances of the topic.
- Exercises must be Python-based and designed so students implement missing pieces.

Scope
- This rule applies when a new programming task set needs to be prepared for learners (e.g., "Typing").

---

# Create python exercises

Read the sections below, create an execution plan, and then implement it.

## What you should make

1. theory.md -- theory for the exercises, ~3 minutes to read
2. theory.md -- translation to Russian
3. 7 files with 3 exercises each and tests on each exercise (see the section "How to create a python source file")
4. __init__.py file

## Execution plan (plane what to produce)

1. Create a plan on what subtopics should be covered, which exercises should be created.
2. Create a list of 7 source files.
3. Review the plan briefly (one short paragraph).

## How to create a python source file

1. Add a docstring on top of the file with a brief description on what this file covers (up to 5 sentences).
2. Add a docstring for every function, method, and class.
3. Add type annotation everywhere.

### Exercises — required format

1. You create stubs of functions/classes/methods etc, the student must implement them.
2. You should add a docstring with requirements.
3. You should provide pydoc tests (see the example).
4. You should create thorough tests on each exercise, use unittest module for the tests. At least 5 tests on each exercise.
5. You should raise the not implemented error in the exercises.

Example:
Input Topic = dictionaries
Output:
```python
def invert_dictionary(d: dict) -> dict:
    """
    Create an inverted dictionary e.q. key becomes a value and value a key. 
    If some value is not unique, the ValueError should be raised
    Is some value can't be a key (unhashable) the Value error should be raised
    >>> invert_dictionary({})
    {}
    
    >>> invert_dictionary({1: "one"})
    {"one": 1}
    
    >>> invert_dictionary({1: 1, 2: 1})
    ValueError
    """
    raise NotImplementedError
```

### Tests
1. Tests should be in the same file as the exercise
2. Thorough tests, at least 3 on each exercise, may add more if needed
3. use the unittest framework, add tests on the bottom of the file like
```python

# -------------------- Tests --------------------
import unittest
class TestRectangle(unittest.TestCase):
    ...
```

## How to create theory.md

1. Finish with the source files creation, read them, and start to create the theory.md
2. Try to cover the topics in the source files in the theory.md