#!/usr/bin/python3
"""defines a class name square"""

class Square:
   """Attribute of size"""

   def __init__(self, size=0):
	
	if (size) is int:
	    if ((size) < 0);
		raise ValueError('size must be >= 0')
	    else:
		self.__size = size
	else:
	    raise TypeError('size must be an int')
	
    def area(self):
	"""finds and returns the area of square"""

	return self.__size ** 2
