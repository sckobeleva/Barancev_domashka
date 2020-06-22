from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):  # переходим на страницу "groups"
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):  # создаем новую группу, заполняем поля, сохраняем
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.CSS_SELECTOR, "[name = ""new""]").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):  # возвращаемся на страницу "groups"
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):   # удаляем первую по счету пустую группу
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_group_page()

