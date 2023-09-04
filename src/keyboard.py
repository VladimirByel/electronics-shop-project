from src.item import Item


class MixinLog:

    def __init__(self):
        """
        Default language is English
        """
        self.__language: str = 'EN'

    def change_lang(self):

        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)


