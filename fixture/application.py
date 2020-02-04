from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def logout(self):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, group):
        wd = self.driver
        # создать группу
        wd.find_element(By.NAME, "new").click()
        # Заполнение форм групп
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name_group)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.driver
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        wd = self.driver
        # Открытие главное страницы
        wd.get("http://localhost/addressbook/")
        wd.set_window_size(1356, 1040)

    def destroy(self):
        self.driver.quit()


