

from barancev_python_for_testing.fixture.application import Application

import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    # Функция инициализации запускает драйвер браузера фикстура