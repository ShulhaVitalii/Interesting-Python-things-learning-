class Point:
  """
  https://stepik.org/lesson/701986/step/1?unit=702087
  Magical methods __setattr__, __getattribute__, __getattr__, __delattr__
  """
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # Using to manage access to the attribute
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Access denied')
        else:
            return object.__getattribute__(self, item)

    # Using to deny creation of local attribute in the class instance
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Wrong attribute name')
        object.__setattr__(self, key, value)

    # Using if the attribute is not exist
    def __getattr__(self, item):
        return False

    # Using for deletion the attribute
    def __delattr__(self, item):
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
a = pt1.y
#pt1.z = 5  # => AttributeError: Wrong attribute name
print(a)
