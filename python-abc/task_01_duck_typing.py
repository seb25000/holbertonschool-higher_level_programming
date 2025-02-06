#!/usr/bin/env python3
import abc
import math


class Shape(abc.ABC):
    """Abstract base class for shapes."""

    @abc.abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abc.abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius: float):
        """
        Initialize a Circle object.

        Args:
            radius (float): The radius of the circle.
        """
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle object.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape: Shape):
    """
    Print the area and perimeter of a shape object.

    Args:
        shape (Shape): An object that has area and perimeter methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
