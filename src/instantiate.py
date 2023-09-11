class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):

        if not kwargs['quantity']:
            self.message = 'Файл item.csv поврежден'
