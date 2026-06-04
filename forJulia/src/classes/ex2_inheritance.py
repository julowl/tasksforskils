"""
Exercise 2 — Inheritance and method overriding

Tasks:
- Implement base class Animal and subclass Dog
- Animal defines name and age, and a speak() method that raises NotImplemented
- Dog should override speak() and maintain additional attribute "breed"; it should call super().__init__ correctly

Run tests by executing this file: python src/ex2_inheritance.py
"""
import unittest

class Animal:
    """Base animal class.

    Attributes:
        name (str): animal's name
        age (int): animal's age in years (non-negative)
    """

    def __init__(self, name: str, age: int):
        """Initialize an Animal.

        Raises:
            ValueError: if age is negative or name is empty
        """
        if not name.strip() or age <= 0:
            raise ValueError('age is negative or name is empty')
        self.name = name.strip().capitalize()
        self.age = age


    def speak(self) -> str:
        """Return the sound this animal makes.

        Subclasses should override this method.
        """
        raise NotImplementedError


class Dog(Animal):
    """Dog subclass with breed attribute."""

    def __init__(self, name: str, age: int, breed: str):
        """Initialize a Dog and call the parent's initializer.

        Raises:
            ValueError: if breed is empty
        """
        if not breed.strip():
            raise ValueError("Breed cannot be empty")

        super().__init__(name, age)
        self.breed = breed


    def speak(self) -> str:
        """Dog's speech should include its name and the bark 'woof'.

        Example: "Rex says woof"
        """
        return f"{self.name} says woof"


# -------------------- Tests --------------------
class TestInheritance(unittest.TestCase):
    def test_animal_validation(self):
        with self.assertRaises(ValueError):
            Animal('', 1)
        with self.assertRaises(ValueError):
            Animal('name', -1)

    def test_dog_inits_and_speaks(self):
        d = Dog('Buddy', 3, 'Beagle')
        self.assertEqual(d.name, 'Buddy')
        self.assertEqual(d.age, 3)
        self.assertEqual(d.breed, 'Beagle')
        self.assertEqual(d.speak(), 'Buddy says woof')

    def test_dog_invalid_breed(self):
        with self.assertRaises(ValueError):
            Dog('x', 1, '')


if __name__ == '__main__':
    unittest.main()
