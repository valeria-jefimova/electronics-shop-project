from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляров класса Phone
        @type number_of_sim: integer
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            raise ValueError('Складывать можно только объекты Phone и дочерние от них')
        return self.quantity + other.quantity


