---
name: Task creation
alwaysApply: false
description: Use this rule if you need to create a new task. For example if the user asks to create a task on the topic of "Typing" use this rule
---

For the topic of {TOPIC} create 7 exercises that highlight different approaches and nuances of the topic.

# Create python exercises

Read the sections, create an execution plan, and then implement it.

## Plan the implementation

1. Create a plan on what subtopics should be covered, which exercises should be created.
2. Create a list of 7 source files
3. Review the plan briefly (one short paragraph).

## How to create a python source file

1. Add a docstring on top of the file with a brief description on what this file covers (up to 5 sentences)
2. Add a docstring for every function, method, and class
3. Add type annotation everywhere

### Exercises
1. You create stubs of functions/classes/methods etc, the student must implement them
2. You should add a docstring with requirements
3. You should provide pydoc tests (see the example)
4. You should create thorough tests on each exercise, use unittest module for the tests. At least 5 tests on each exercise
5. You should raise the not implemented error in the exercises

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
```

Requirements and steps:
1. Create a short plan of what needs to be covered for {TOPIC}.
2. Review the plan briefly (one short paragraph).
3. Create 5–7 source files with code and placeholders that students must fill.
   - Save all files in the directory src/<shortTopicName>.
   - Each file should implement one exercise or helper module.
   - Use "raise NotImplemented" where the student must implement code.
   - Include docstrings for every function or method the student must implement, describing inputs, outputs, and behavior.
4. Begin each exercise with a theory section limited to ~3 minutes of reading (concise explanation).
   - Also, create two theory files in src/<shortTopicName>: theory.md and theory_ru.md (Russian translation).
5. For each exercise file:
   - Provide code skeletons with clear placeholders.
   - Add comprehensive unittests using Python's unittest module.
   - Create many tests covering normal cases, edge cases, error handling, and incorrect inputs.
6. Add a short summary at the end of the whole exercise set.
7. Ensure tests run with unittest discovery (e.g., tests named test_*.py).
8. Use clear filenames and a shortTopicName consistent with {TOPIC} (lowercase, no spaces).
9. Do not include solved implementations—only placeholders where work is required and tests that will fail until implemented.
10. Keep the entire package self-contained; tests import from the src/<shortTopicName> package.

Deliverables to output now:
- A plan section listing topics to cover (bullet points).
- A brief review of the plan.
- A file list for src/<shortTopicName> with brief descriptions.
- For each file, output its full content (plain text), including:
  - Module docstring.
  - Code skeleton with placeholders and "raise NotImplemented" exactly where the student must implement.
  - Docstrings for functions/methods to implement.
- For each test file, include many unittest.TestCase methods covering diverse scenarios.
- theory.md and theory_ru.md contents.
- A short summary paragraph concluding the exercise set.

Do not include any additional explanation beyond these deliverables.

