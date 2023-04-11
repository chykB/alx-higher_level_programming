#!/usr/bin/python3

"""Creates a class that can be used as a base class for other geometry-related classes"""

class BaseGeometry:
	"""Creates a class that can be used as a base class for other geometry-related classes"""
	
	def area(self):
	"""
	Calculate the area of the geometry.
        
        Raises:
            Exception: If the area() method is not implemented in the derived class.
        """
	raise Exception("area() is not implemented")
