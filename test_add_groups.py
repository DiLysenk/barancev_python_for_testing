from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group
import unittest
from application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    # Функция инициализации запускает драйвер браузера фикстура


def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name_group="buranzev22", header="первый", footer="второй"))
    app.open_groups_page()
    app.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name_group="", header="", footer=""))
    app.open_groups_page()
    app.logout()



    """ функции для тестов"""






if __name__ == '__main__':
    unittest.main()
