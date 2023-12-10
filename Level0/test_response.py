# Generated by Selenium IDE
import pytest
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPerformance():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_1(self):
        print(sys._getframe(0).f_code.co_name)
        try:
            self.driver.get("https://sandbox.moodledemo.net/")
            self.driver.set_window_size(924, 802)
            self.driver.find_element(By.LINK_TEXT, "Log in").click()
            self.driver.find_element(By.ID, "username").click()
            self.driver.find_element(By.ID, "username").clear()
            self.driver.find_element(By.ID, "username").send_keys("student")
            self.driver.find_element(By.ID, "password").click()
            self.driver.find_element(By.ID, "password").send_keys("sandbox")
            self.driver.find_element(By.ID, "loginbtn").click()
            self.driver.find_element(By.ID, "user-menu-toggle").click()
            self.driver.find_element(By.LINK_TEXT, "Calendar").click()
            self.driver.find_element(By.XPATH, "//button[contains(.,\'New event\')]").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "id_name").click()
            self.driver.find_element(By.ID, "id_name").send_keys("Test Event")
            self.driver.find_element(By.ID, "id_timestart_day").click()
            dropdown = self.driver.find_element(By.ID, "id_timestart_day")
            dropdown.find_element(By.XPATH, "//option[. = '7']").click()
            self.driver.find_element(By.XPATH, "//button[contains(.,\'Save\')]").click()
            self.driver.find_element(By.ID, "user-menu-toggle").click()
            self.driver.find_element(By.LINK_TEXT, "Log out").click()
            return True
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.driver.find_element(By.ID, "user-menu-toggle").click()
            self.driver.find_element(By.LINK_TEXT, "Log out").click()
            return False
        
    def test_2(self):
        print(sys._getframe(0).f_code.co_name)
        try:
            self.driver.get("https://sandbox.moodledemo.net/")
            self.driver.set_window_size(1054, 802)
            self.driver.find_element(By.LINK_TEXT, "Log in").click()
            self.driver.find_element(By.ID, "username").click()
            self.driver.find_element(By.ID, "username").clear()
            self.driver.find_element(By.ID, "username").send_keys("teacher")
            self.driver.find_element(By.ID, "password").click()
            self.driver.find_element(By.ID, "password").send_keys("sandbox")
            self.driver.find_element(By.ID, "loginbtn").click()
            self.driver.find_element(By.LINK_TEXT, "My courses").click()
            self.driver.find_element(By.ID, "user-menu-toggle").click()
            self.driver.find_element(By.LINK_TEXT, "Log out").click()
            self.driver.close()
            return True
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.driver.find_element(By.ID, "user-menu-toggle").click()
            self.driver.find_element(By.LINK_TEXT, "Log out").click()
            return False
        
    def test(self, *test_list):
        result = []
        for test in test_list:
            result.append(test())
        fail_test_name = []
        for i in range(0, len(result)):
            if not result[i]:
                fail_test_name.append(test_list[i].__name__)

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        return f"""
        \n- Test update course (Level 0)--\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """
        
    def run(self):

        self.setup_method(None)

        result = self.test(
        self.test_1,
        self.test_2
       
        )

        self.teardown_method(None)

        return result

performance = TestPerformance()
print(performance.run())