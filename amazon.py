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

class amazon(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_amazon(self):
        success = True
        wd = self.wd
        wd.get("https://www.amazon.com/ref=nav_logo")
        wd.find_element_by_xpath("//div[@id='_1jVj4MlPpgwTlJrcHO8kg']/div[2]/a/div/img").click()
        wd.find_element_by_link_text("Technical details").click()
        wd.find_element_by_link_text("Sell on Amazon").click()
        wd.find_element_by_link_text("Start selling").click()
        wd.back()
        wd.back()
        wd.back()
        wd.find_element_by_link_text("Fire Tablets").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
