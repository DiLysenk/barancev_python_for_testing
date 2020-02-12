from barancev_python_for_testing.model.group import Group


def test_modify_group_name(app):

    app.group.open_groups_page()
    app.group.modify_first_group(Group(name_group="New group"))
    app.group.open_groups_page()


def test_modify_group_header(app):

    app.group.open_groups_page()
    app.group.modify_first_group(Group(header="New header"))
    app.group.open_groups_page()