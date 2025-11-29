
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
        """Print an introduction of the dog.   """
        print(f"hi, I´m {self.name}, a {self.age}-year-old {self.breed}.")

        Mr.King = Dog('Mr.King', 'Golden Retriever', 6)
        Mr.King.introduce()



