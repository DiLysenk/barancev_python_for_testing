from selenium import webdriver
from selenium.webdriver.common.by import By
from barancev_python_for_testing.fixture.session import SessionHelper
from barancev_python_for_testing.fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)



    def open_home_page(self):
        wd = self.driver
        # Открытие главное страницы
        wd.get("http://localhost/addressbook/")
        wd.set_window_size(1356, 1040)

    def destroy(self):
        self.driver.quit()


