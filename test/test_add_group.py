from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
# в список символов можно еще добавить + string.punctuation

# полный перебор всех возможных случаев: 3 поля, 2 значения (пустое и рандомное) - запустится 8 тестов
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#    for footer in ["", random_string("footer", 20)]
#]

# второй вариант рандомных данных
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])    # 3 параметр выводит в отчете питест тестовые данные, подготовленные функцией __repr__
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
