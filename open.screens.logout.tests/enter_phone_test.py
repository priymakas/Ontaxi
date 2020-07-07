import allure
import conftest
from elements import element
import time


@allure.feature("Enter phone")
@allure.story("Open autorisation")
@allure.severity("critical")
class TestPhoneEnter:
    @allure.step("Открыть меню")
    def test_open_drawer(self):
        conftest.find_by_id(element.MENU_BTN)
        time.sleep(2)
        assert conftest.driver.find_element_by_id(element.ENTER_BTN).is_displayed()


    @allure.step("Нажать на кнопку войти")
    def test_click_login(self):
        conftest.find_by_id(element.ENTER_BTN)
        time.sleep(2)
        assert conftest.driver.find_element_by_id("termsOfServiceTextView").is_displayed()

    @allure.step("ввести номер телефона")
    def test_enter_phone(self):
        conftest.test_phone_number_enter("990882876")
        time.sleep(5)
# # НУжно придумать проверку
    @allure.step("Согласиться с условиями")
    def test_turn_terms_switcher(self):
        conftest.find_by_id(element.TERMS_AND_CONDITION_SWITCHER)
        assert conftest.driver.find_element_by_id(element.TERMS_AND_CONDITION_SWITCHER).is_enabled()

    def stop_test(self):
        conftest.tearDown(self)
