# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class utest(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_utest(self):
        success = True
        wd = self.wd
        wd.get("https://www.utest.com/")
        wd.find_element_by_link_text("ACCEPT").click()
        wd.find_element_by_xpath("//div[@class='nav-bar-wrapper']//a[.='Sign in']").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("swladuli@gmail.com")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("Vladis1972")
        wd.find_element_by_css_selector("label").click()
        if not wd.find_element_by_id("rememberMe").is_selected():
            wd.find_element_by_id("rememberMe").click()
        wd.find_element_by_css_selector("button.has-spinner").click()
        ActionChains(wd).double_click(wd.find_element_by_link_text("Notifications")).perform()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//div[@class='brand']/a/img")).perform()
        wd.find_element_by_css_selector("p.feed-item-description.clickable").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
