class Square:
    '''represent a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''initialize a new square

        Args:
            size (int): the size of the square created
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''get the current size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gset the current position square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the area of square.'''
        return (self.__size * self.__size)

    def my_print(self):
        '''print the square with character'''
        for i in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
