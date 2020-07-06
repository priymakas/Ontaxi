from appium import webdriver

caps = {"platformName": "Android", "automationName": "Appium",
        "app": "D:\\AndroidClient\\app\\build\\outputs\\apk\\debug\\ontaxi-client-5.1.3-release.apk",
        "autoGrantPermissions": True}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


def test_drawer(element_id):
    driver.find_element_by_id(element_id).click()
    assert driver.find_element_by_id(element_id).is_enabled()
