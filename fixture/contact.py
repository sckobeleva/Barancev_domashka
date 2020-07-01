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
        self.fill_contact_form(contact)
        driver.find_element(By.NAME, "submit").click()
        self.app.open_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):  # изменяем поля контакта, только если они не пустые
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_contact_by_index(self, index):   # аходим контакт по индексу и удаляем
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_elements(By.NAME,"selected[]")[index].click()
        driver.find_element(By.CSS_SELECTOR, "[value=""Delete""]").click()
        alert = driver.switch_to.alert
        alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):   # заполняем поля контакта
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.faxphone)

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

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        driver.find_element(By.CSS_SELECTOR, "[value=""Update""]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index): # находим контакт по индексу и открываем редактирование
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index): # находим контакт по индексу и открываем на просмотр
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()





