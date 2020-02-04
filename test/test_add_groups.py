

from barancev_python_for_testing.fixture.application import Application
from barancev_python_for_testing.model.group import Group
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

