import selenium
from selenium.webdriver.common.by import By

class GroupHelper:


    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.driver
        # создать группу
        wd.find_element(By.NAME, "new").click()
        # Заполнение форм групп
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name_group)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()


    def delete_first_group(self):
        wd = self.app.driver
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()

    def open_groups_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "groups").click()
