import allure
import conftest

@allure.feature("Open menu")
@allure.story("Open drawer")
@allure.severity("minor")
class TestMenuOpen:
    @allure.step("Открыть меню")
    def test_step_drawer(self):
        conftest.find_by_id("btnMenu")

    def stop_test(self):
        conftest.tearDown(self)

