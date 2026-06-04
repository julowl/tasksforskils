For loops in Python — short theory (≈ 3 minutes)

- Purpose: for loops iterate over items of any iterable (lists, tuples, strings, dicts, files, generators).
- Basic syntax:

  for item in iterable:
      # do something with item

- Range: range(start, stop[, step]) produces integers. Common patterns:
  - for i in range(n):  # 0..n-1
  - for i in range(a, b):  # a..b-1
  - for i in range(a, b, step)

- Useful built-ins with loops:
  - enumerate(iterable)  -> yields (index, item)
  - zip(*iterables)  -> pairs/triples of elements
  - reversed(seq)  -> iterate in reverse order

- Control statements:
  - break: exit loop early
  - continue: skip to next iteration
  - else clause on loops: executed if loop completes normally (no break)

- Nested loops: use loops inside loops to work with matrices or Cartesian products.

- Generators and iteration: you can yield from a loop to produce an iterator lazily.

Tips:
- Prefer iterating directly over items, not over indices, unless you need the index.
- Use list/dict comprehensions when you just build a collection from a loop — they are concise and often faster.

This short guide highlights the patterns you'll practice in the exercises that follow.
