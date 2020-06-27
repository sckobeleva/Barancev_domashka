from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):  # создаем новую группу, заполняем поля, сохраняем
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.CSS_SELECTOR, "[name = ""new""]").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):    # считаем количество групп в списке
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    def change_field_value(self, field_name, text): # заполняем поля группы, только если они не пустые
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):   # удаляем первую по счету пустую группу
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):   # заполняем поля группы
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    group_cache = None

    def get_group_list(self):   # получаем список групп
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)

    def modify_first_group(self, new_group_data):   # редактируем форму и сохраняем изменения
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element(By.NAME, "update").click()
        self.return_to_group_page()
        self.group_cache = None

    def open_groups_page(self):  # переходим на страницу "groups"
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements(By.CSS_SELECTOR, "[name = ""new""]"))>0 ):
            driver.find_element(By.LINK_TEXT, "groups").click()

    def return_to_group_page(self):  # возвращаемся на страницу "groups"
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def select_first_group(self):   # находим и выбираем первую в списке группу
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()
