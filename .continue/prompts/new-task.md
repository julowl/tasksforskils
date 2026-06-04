Continue the previous task and complete it now.

For the topic of {TOPIC} create 5 exercises that highlight different approaches and nuances of the topic.

Requirements and steps:
1. Create a short plan of what needs to be covered for {TOPIC}.
2. Review the plan briefly (one short paragraph).
3. Create 5–7 source files with code and placeholders that students must fill.
   - Save all files in the directory src/<shortTopicName>.
   - Each file should implement one exercise or helper module.
   - Use "raise NotImplemented" where the student must implement code.
   - Include docstrings for every function or method the student must implement, describing inputs, outputs, and behavior.
4. Begin each exercise with a theory section limited to ~3 minutes of reading (concise explanation).
   - Also create two theory files in src/<shortTopicName>: theory.md and theory_ru.md (Russian translation).
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

