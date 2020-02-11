from barancev_python_for_testing.fixture.application import Application
from barancev_python_for_testing.model.group import Group
from barancev_python_for_testing.fixture.group import GroupHelper
import pytest


def test_delete_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create_group(Group(name_group="", header="", footer=""))
    app.group.open_groups_page()
    app.session.logout()
