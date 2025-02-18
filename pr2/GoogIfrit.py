class GoodIfrit:
    def __init__(self, height, name, goodness):
        # Инициализация экземпляра класса с высотой, именем и добротой
        self.height = height
        self.name = name
        self.goodness = goodness

    def change_goodness(self, amount):
        # Изменение доброты на указанную величину
        self.goodness += amount
        # Доброта не может быть отрицательной, в этом случае становится равной 0
        if self.goodness < 0:
            self.goodness = 0

    def __add__(self, number):
        # Прибавление числа к высоте, создание нового экземпляра с измененной высотой
        return GoodIfrit(self.height + number, self.name, self.goodness)

    def __call__(self, value):
        # Возвращение значения: аргумент * доброта / высота
        return value * self.goodness // self.height

    def __str__(self):
        # Возвращение строки вида: “Good Ifrit <name>, height <высота>, goodness <доброта>”
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"

    def __lt__(self, other):
        # Сравнение по доброте, затем по высоте, затем по имени по алфавиту
        if self.goodness != other.goodness:
            return self.goodness < other.goodness
        if self.height != other.height:
            return self.height < other.height                   
        return self.name < other.name

    def __le__(self, other):
        # Сравнение по доброте, затем по высоте, затем по имени по алфавиту
        return self < other or self == other

    def __eq__(self, other):
        # Сравнение по доброте, затем по высоте, затем по имени по алфавиту
        return self.goodness == other.goodness and self.height == other.height and self.name == other.name

    def __ne__(self, other):
        # Сравнение по доброте, затем по высоте, затем по имени по алфавиту
        return not self == other

    def __gt__(self, other):
        # Сравнение по доброте, затем по высоте, затем по имени по алфавиту
        return not self <= other

    def __ge__(self, other):
        # Сравнение по доброте, затем по высоте, затем по имени по алфавиту
        return not self < other

# ввод 1
gi = GoodIfrit(80, "Hazrul", 3)
gi.change_goodness(4)
print(gi)
gi1 = gi + 15
print(gi1)
print(gi(31))

# ввод 2
gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)
gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1)