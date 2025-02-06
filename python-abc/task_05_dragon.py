#!/usr/bin/env python3

class SwimMixin:
    """
    A mixin class that provides swimming functionality.
    """
    def swim(self):
        """
        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying functionality.
    """
    def fly(self):
        """
        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon that can swim and fly, inheriting from
    SwimMixin and FlyMixin.
    """
    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
