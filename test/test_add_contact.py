from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="aaa", middlename="aaa", lastname="aaa", nickname="aaa"))
