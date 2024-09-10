class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name: str, weight: float, author: str, date: str):
        super().__init__(name, weight)
        self.date = date
        self.author = author


class Computer(Thing):
    def __init__(self, name: str, weight: float, memory: int, cpu: str):
        super().__init__(name, weight)
        self.cpu = cpu
        self.memory = memory


class Auto(Thing):
    def __init__(self, name: str, weight: float, dims: tuple[int | float]):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(
            self,
            name: str, weight: float,
            dims: tuple[int | float],
            model: str, old: int):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(
            self,
            name: str, weight: float,
            dims: tuple[int | float],
            model: str, wheel: bool):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


# th1 = Thing(name, weight)
# obj1 = ArtObject(name, weight, author, date)  # author - автор (строка); date - дата создания (строка)
# obj2 = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое число); cpu - тип процессора (строка)
# obj3 = Auto(name, weight, dims)               # dims - габариты, кортеж (width, length, height) - вещественные или целые числа
# auto1 = Mercedes(name, weight, dims, model, old) # model - модель (строка); old - время использования, в годах (целое число)
# auto2 = Toyota(name, weight, dims, model, wheel) # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный

print(Mercedes('мерс', 1500, (6, 2.4, 1.6), '600', 12).dims[2])
