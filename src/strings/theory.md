Strings in Python — short theory

This short theory (~3 minutes) covers the basics and some advanced topics you'll see in the exercises.

1. What is a string
- A string is an immutable sequence of Unicode characters in Python.
- You can create strings with single ('...'), double ("..."), or triple ('''...''' or """...""") quotes.

2. Basic operations
- Length: len(s)
- Indexing and slicing: s[i], s[start:stop:step]
- Concatenation: s1 + s2, repetition: s * n

3. Searching and parsing
- Membership: 'sub' in s
- Finding: s.find(sub) -> index or -1; s.index(sub) raises if not found
- Starts/ends: s.startswith(prefix), s.endswith(suffix)

4. Formatting
- Old-style: '%s %d' % (s, n)
- str.format: "{:.2f}".format(1.234)
- f-strings (Python 3.6+): f"{value:.2f}" — recommended for readability and expression embedding

5. Escape sequences and raw strings
- Backslash '\\' escapes special characters, e.g. '\\n', '\\t', '\\''
- Raw strings r"..." prevent backslash interpretation (useful for Windows paths and regex patterns)

6. Unicode and bytes
- Strings are Unicode; use ord() and chr() to go between characters and codepoints
- Encode to bytes: s.encode('utf-8'); decode: b.decode('utf-8')
- Normalization: unicodedata.normalize('NFC', s) to combine characters reliably

7. Useful methods
- split(), join(), replace(), translate(), maketrans(), strip(), lstrip(), rstrip()
- format specifiers for alignment, width, precision: '{:0>3d}', '{:^10}', '{:.2f}'

This theory informs the exercises in this package.