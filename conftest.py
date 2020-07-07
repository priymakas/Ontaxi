from appium import webdriver
import time
import allure

caps = {"platformName": "Android", "automationName": "Appium",
        "app": "D:\\Testapk\\ontaxi-client-5.1.3-release.apk",
        "autoGrantPermissions": True}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


def find_by_id(element_id):
    driver.find_element_by_id(element_id).click()


def tearDown(self):
    self.driver.hide_keyboard()
    self.driver.quit()


def find_by_text(element_id, sleep_time, ustext, rutext):
    for item in driver.find_elements_by_id(element_id):
        if (str(item.text) == str(ustext)) or (str(item.text) == str(rutext)):
            item.click()
            time.sleep(sleep_time)



def find_phone_in_field(phone):
    for item in driver.find_elements_by_id("textInputPhone"):
        if str(item.text) == str(phone):
            return True


def test_phone_number_enter(phone):
    for key_button in phone:
        key = int(key_button)
        key_interpreter = {0: 7, 1: 8, 2: 9, 3: 10, 4: 11, 5: 12, 6: 13, 7: 14, 8: 15, 9: 16}
        driver.press_keycode(key_interpreter[key])



def test_search_area_and_enter_code(id, sms, sleep_time):
    enter_code_area = driver.find_element_by_id(id)
    enter_code_area.send_keys(sms)
    time.sleep(sleep_time)

