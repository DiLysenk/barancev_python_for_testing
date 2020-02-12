

def test_del_first_group(app):
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.group.open_groups_page()

