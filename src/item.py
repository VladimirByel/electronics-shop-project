import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[0:10]
        else:
            self.__name = value

    def __repr__(self):
        return f"""{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"""

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('../src/items.csv', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            print("Отсутствует файл item.csv")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None
