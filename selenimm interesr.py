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

class selenimm interesr(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_selenimm interesr(self):
        success = True
        wd = self.wd
        wd.get("https://www.google.com/")
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").clear()
        wd.find_element_by_id("lst-ib").send_keys("x")
        wd.find_element_by_xpath("//div[@id='sbse1']//b[.='iaomi redmi note 5']").click()
        ActionChains(wd).double_click(wd.find_element_by_css_selector("center")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
