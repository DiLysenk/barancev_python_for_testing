from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group
import unittest
from application import Application

class test_add_group(unittest.TestCase):

    # Функция инициализации запускает драйвер браузера фикстура
    def setup_method(self):
        self.app = Application()


      def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name_group="buranzev22", header="первый", footer="второй"))
        self.open_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name_group="", header="", footer=""))
        self.open_groups_page()
        self.logout()

    # Функция закрытия
    def teardown_method(self):
        self.app.destroy()


    """ функции для тестов"""






if __name__ == '__main__':
    unittest.main()
