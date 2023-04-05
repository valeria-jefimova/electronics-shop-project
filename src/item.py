import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.all.append(self)

    @property  #getter
    def name(self):
        return self.__name

    @name.setter  #setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return int(self.price) * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        with open('./src/items.csv', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))
                print(row)

    @staticmethod
    def string_to_number(value: str) -> int:
        """Статический метод, возвращающий число из числа-строки"""
        return round(int(value[0]), 2)

    def __repr__(self) -> str:
        """Магический метод __repr__ переопределение"""
        #self.__class__.name - property object at 0x10a1915d0>
        #self.__class__.__name__ - 'Item_
        return f"{self.__class__.__name__}('{self.__name}', {int(self.price)}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    def __add__(self, other: 'Item') -> int:
        if not isinstance(other, Item):
            raise TypeError('Нельзя складывать Phone или Item с экземплярами не Phone или Item классов.')
        return self.quantity + other.quantity






