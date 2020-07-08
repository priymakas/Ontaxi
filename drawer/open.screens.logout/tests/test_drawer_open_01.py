import allure
import conftest
from elements import element
import pytest
@allure.feature("Open menu")
@allure.story("Open drawer")
@allure.severity("minor")
class TestMenuOpen:
    def setup_function(self):
        conftest.driver.start_client()

    @allure.step("Открыть меню")
    def test_step_drawer(self):
        conftest.find_by_id(element.MENU_BTN)
        conftest.driver.implicitly_wait(5)
        conftest.driver.find_element_by_id(element.MENU_BTN)
        assert conftest.driver.find_element_by_id(element.MENU_BTN).is_displayed()
