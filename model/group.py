from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self): # получаем строковое представление объекта
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):    # сравниваем группы по смыслу, а не по физ.расположению, чтобы сравнение не падало
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):  # получаем ключ, по которому будем сравнивать группы
        if self.id:
            return int(self.id)
        else:
            return maxsize