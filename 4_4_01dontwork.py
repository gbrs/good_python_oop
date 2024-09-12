class Animal:
    def __init__(self, name, kind, old):
        self.__old = old
        self.__kind = kind
        self.__name = name

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, value):
            self.__name = value

        @property
        def kind(self):
            return self.__kind

        @kind.setter
        def kind(self, value):
            self.__kind = value

        @property
        def old(self):
            return self.__old

        @kind.setter
        def old(self, value):
            self.__old = value


animals = [
        Animal('Васька', 'дворовый кот', 5),
        Animal('Рекс', 'немецкая овчарка', 8),
        Animal('Кеша', 'попугай', 3)]



print(animals[1].kind)


"""
an = Animal(name, kind, old)
Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3
"""
