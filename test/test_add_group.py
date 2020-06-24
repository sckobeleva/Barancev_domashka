from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="444", header="444", footer="444"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
