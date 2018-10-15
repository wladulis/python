# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.google.com/")
    wd.find_element_by_id("lst-ib").click()
    wd.find_element_by_id("lst-ib").click()
    wd.find_element_by_id("lst-ib").clear()
    wd.find_element_by_id("lst-ib").send_keys("x")
    wd.find_element_by_xpath("//div[@id='sbse1']//b[.='iaomi redmi note 5']").click()
    ActionChains(wd).double_click(wd.find_element_by_css_selector("center")).perform()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
