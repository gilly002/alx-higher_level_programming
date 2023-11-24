#!/usr/bin/python3

"""Define a class Square."""
class Square:
    """Represent a new square."""
    def _int_(self, size=0):
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
        raise TypeError("size must be an integer")
        elif size < 0:
        raise ValueError("size must be an integer")
        self._size = size
