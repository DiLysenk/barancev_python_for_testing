
from barancev_python_for_testing.model.group import Group



def test__add_group(app):

    app.group.open_groups_page()
    app.group.create_group(Group(name_group="buranzev22", header="первый", footer="второй"))
    app.group.open_groups_page()


def test__add_empty_group(app):

    app.group.open_groups_page()
    app.group.create_group(Group(name_group="", header="", footer=""))
    app.group.open_groups_page()


 