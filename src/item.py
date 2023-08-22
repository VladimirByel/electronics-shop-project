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
            self.__name = value[0:9]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Item.all.append(Item(row['name'], row['price'], row['quantity']))

    
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
        if '.' in number:
            return int(float(number))
        elif number.isnumeric():
            return int(number)
        else:
            print('not a number')


