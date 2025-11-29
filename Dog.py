"""dog.py - Dog class exercise for Chapter 9.

Test run (2025-11-29):
    python dog.py

Output:
    hi, I´m Mr. King, a 6-year-old Golden Retriever.
    hi, I´m Benji, a 3-year-old Beagle.
    Mr. King is now sitting.
    Benji rolled over!
"""


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name: str, breed: str, age: int) -> None:
        """Initialize attributes to describe a dog."""
        self.name = name
        self.breed = breed
        self.age = age

    def sit(self) -> None:
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def introduce(self) -> None:
        """Print an introduction of the dog."""
        print(f"Hi, I´m {self.name}, a {self.age}-year-old {self.breed}.")


if __name__ == "__main__":
    mr_king = Dog("Mr. King", "Golden Retriever", 6)
    benji = Dog("Benji", "Beagle", 3)

    mr_king.introduce()
    benji.introduce()
    mr_king.sit()
    benji.roll_over()

