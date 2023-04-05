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
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = value

    def __repr__(self):
        # data = super().__repr__()
        # return data.replace(')', f', {self.number_of_sim}
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"
