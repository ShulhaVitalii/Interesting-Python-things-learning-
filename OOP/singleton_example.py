class Singleton:
    """
    https://www.youtube.com/watch?v=PxOfMkw962E
    """
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


s = Singleton()
game1 = Game('Game1')
game2 = Game('Game2')
print(game1.name)
print(game2.name)
