from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self):  # переходим на страницу "add new" для создания контакта
        driver = self.app.driver
        if not (driver.current_url.endswith("/edit.php") and len(driver.find_elements_by_name("submit")) > 0):
            driver.find_element(By.LINK_TEXT, "add new").click()

    def count(self):    # получаем количество контактов в списке
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements(By.CSS_SELECTOR, "td input"))

    def create(self, contact):  # заполняем поля в карточке, сохраняем
        driver = self.app.driver
        self.add_new_contact()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").send_keys(contact.homephone)
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").send_keys(contact.mobilephone)
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").send_keys(contact.workphone)
        driver.find_element(By.NAME, "fax").click()
        driver.find_element(By.NAME, "fax").send_keys(contact.faxphone)
        driver.find_element(By.NAME, "submit").click()
        self.app.open_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):   # получаем список контактов
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cache = []
            for elem in driver.find_elements_by_name("entry"):
                id = elem.find_element_by_name("selected[]").get_attribute('id')
                lastname = elem.find_elements_by_css_selector("td")[1].text
                firstname = elem.find_elements_by_css_selector("td")[2].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=str(id)))
        return list(self.contact_cache)

    #def open_contact_to_edit_by_index(self, index): # находим и открываем контакт на редактирование по индексу


    #def open_contact_to_view_by_index(self, index): # находим и открываем контакт на просмотр по индексу






