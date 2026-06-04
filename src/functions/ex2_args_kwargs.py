"""Exercise 2 — *args and **kwargs

Implement functions that demonstrate variable positional and keyword arguments.

Placeholders use 'raise NotImplemented'.
"""

from typing import Dict


def concat(*parts: str, sep: str = ' ') -> str:
    """Concatenate all provided parts using the separator sep.

    Args:
        *parts: any number of string parts to join
        sep: separator placed between parts

    Returns:
        Joined string. If no parts are provided, return an empty string.
    """
    if len(parts) == 0:
        return ""
    result = ""
    for i, part in enumerate(parts):
        if i > 0:
           result += sep
        result += part
    return result



def build_profile(name: str, **attrs) -> Dict[str, object]:
    """Build and return a dictionary representing a person profile.

    The result must always include the 'name' key and then all provided attrs.

    Args:
        name: the person's name
        **attrs: arbitrary profile attributes (age, city, jobs, ...)

    Returns:
        A dict containing at least {'name': name} plus attrs
    """
    least = {'name': name}
    for key, value in attrs.items():
        least[key] = value
    return least


# --- Tests for exercise 2 ---

def test_concat():
    assert concat('a', 'b', 'c') == 'a b c'
    assert concat('a', 'b', sep='-') == 'a-b'
    assert concat() == ''


def test_build_profile():
    p = build_profile('Alice', age=30, city='London')
    assert p['name'] == 'Alice'
    assert p['age'] == 30
    assert p['city'] == 'London'
    # Ensure other keys not present
    assert 'unknown' not in p


if __name__ == '__main__':
    test_concat()
    test_build_profile()
    print('ex2_args_kwargs: tests passed (quick)')
