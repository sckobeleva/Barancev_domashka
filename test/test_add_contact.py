from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="aaa", middlename="aaa", lastname="aaa", nickname="aaa"))
    app.session.logout()