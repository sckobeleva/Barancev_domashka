from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):  # переходим на страницу "add new"
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):  # заполняем поля в карточке, сохраняем
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        driver.find_element(By.NAME, "submit").click()
