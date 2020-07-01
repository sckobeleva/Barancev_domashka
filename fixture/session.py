from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def ensure_login(self, username, password): # логин, если мы не залогинены, или залогинены не под тем пользователем
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):    # разлогин, только если мы залогинены
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self): # проверяем, что мы залогинены
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username): # проверяем, что мы залогинены под конкр. пользователем
        driver = self.app.driver
        return self.is_logged_user() == username

    def is_logged_user(self):
        driver = self.app.driver
        return driver.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

    def login(self, username, password):  # логинимся
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):  # разлогиниваемся
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()



