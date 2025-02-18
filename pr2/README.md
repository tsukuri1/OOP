(12) Класс Добрый Ифрит (Goodlfrit)
Экземпляр класса инициализируется с аргументами: высота, имя, доброта.
Класс должен реализовывать функциональность
— change_goodness(value) — менять доброту на указанную величину; не может стать отрицательной, в этом случае становится равной О;
— к экземпляру класса можно прибавить число: (gi1 — gi + number), создается новый экземпляр с высотой, большей на величину number, остальные характеристики те же;
— экземпляр класса можно вызвать с аргументом, возвращается значение:
аргумент * доброта высота // высота
_str_() — возвращает строку вида:
"Good Ifrit <имя>, height <высота>, goodness <доброта>"
— экземпляры можно сравнивать между собой: сначала по доброте, затем по высоте, затем по имени по алфавиту; для этого нужно реализовать методы сравнения:
Ввод:
qi = GoodIfrit(80, "Hazrul", 3)
gi.change_goodness (4)
print(gi)
gi1 = gi + 15
print (gi1)
print (gi(31))
Вывод:
Good Ifrit Hazrul, height 80, goodness 7
Good Ifrit Hazrul, height 95, goodness 7
2
Ввод:
gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)
gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1, sep='\n')
Вывод:
False
True
Good Ifrit Hazrul, height 80, goodness 3
Good Ifrit Dalziel, height 80, goodness 3