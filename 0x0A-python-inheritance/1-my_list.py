#!/usr/bin/python3
"""Creates an inherited list class MyList."""


class MyList(list):
    """Custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""

        self.sort()
	print(self)
