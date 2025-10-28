from __future__ import annotations
from math import isclose
from exercise1 import Vector

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self._coordinates = Vector([x, y])

    @property
    def x(self) -> float:
        return self._coordinates[0]

    @property
    def y(self) -> float:
        return self._coordinates[1]

    # Task A Solution: Implement In-Place Addition
    def __iadd__(self, other: Vector) -> "Point2D":
        # This line uses the Vector's __add__ method (which returns a new Vector) 
        # and reassigns the internal _coordinates attribute.
        self._coordinates = self._coordinates + other
        return self
    
    def __isub__(self, other: Vector) -> "Point2D":
        # Use the Vector's __sub__ method to perform subtraction,
        # then update the internal _coordinates attribute.
        self._coordinates = self._coordinates - other
        return self


def test_point_construction() -> None:
    point = Point2D(1.0, 42.0)
    assert point.x == 1.0
    assert point.y == 42.0


def test_point_vector_addition() -> None:
    point = Point2D(1.0, 2.0)
    # Task A: make the test below pass (implement __iadd__)
    point += Vector([1.1, 2.2])
    assert isclose(point.x, 2.1)
    assert isclose(point.y, 4.2)


def test_point_vector_subtraction() -> None:
    point = Point2D(1.0, 2.0)
    # Task B: make the test below pass (implement __isub__)
    point -= Vector([1.1, 2.2])
    assert isclose(point.x, -0.1)
    assert isclose(point.y, -0.2)

