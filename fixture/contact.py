from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
                all_phones = elem.find_elements_by_css_selector("td")[5].text
                all_phones2 = all_phones.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=str(id),
                                                  homephone=all_phones2[0], mobilephone=all_phones2[1],
                                                  workphone=all_phones2[2]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_to_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)

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





