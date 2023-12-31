# Generated by Selenium IDE
import pytest
import time
import json
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class TestEditQuizTime():
    def __init__(self, data):
        self.data = data
        self.first_run = True
        
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
        
    def precondition(self):
        self.driver.get("https://school.moodledemo.net/")
        self.driver.set_window_size(1056, 804)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        if self.first_run:
            self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
            self.driver.find_element(By.ID, "username").send_keys("")
            self.driver.find_element(By.ID, "password").click()
            self.driver.find_element(By.ID, "username").click()
            self.driver.find_element(By.ID, "username").send_keys("teacher")
            self.driver.find_element(By.ID, "password").click()
            self.first_run = False
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(5)
    
    def logout(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(5)
        
    def testEditTime(self, limitTime: str):
        try:
            self.precondition()
            self.driver.find_element(By.CSS_SELECTOR, ".searchbar input.form-control").send_keys("activity")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//div[1]/div/div/div/a/span[3]").click()
            self.driver.find_element(By.LINK_TEXT, "Quizzes").click()
            self.driver.find_element(By.XPATH, "//li[@id=\'module-703\']/div/div[2]/div/div/div/div/a").click()
            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, "Settings").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "collapseElement-1").click()
            time.sleep(5)
            enableItem = self.driver.find_element(By.ID, "id_timelimit_enabled")
            if enableItem.is_selected() == False:
                enableItem.click()
            elements = self.driver.find_element(By.ID, "id_timelimit_number")
            if elements:
                self.driver.find_element(By.ID, "id_timelimit_number").click()
                self.driver.find_element(By.ID, "id_timelimit_number").send_keys(limitTime)
                self.driver.find_element(By.ID, "id_submitbutton2").click()
                time.sleep(5)
                self.logout()
                return True
            else:
                self.logout()
                return False
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.logout()
            return False
        
    def test(self, test_list: list):
        result = []
        for test in test_list:
            test_name = test['test_name']
            print(test_name)
            result.append(self.testEditTime(test['test_data']['limitTime']))

        fail_test_names = [test['test_name'] for i, test in enumerate(test_list) if not result[i]]

        if fail_test_names:
            fail_test_name_str = 'FAILED:\n\t' + '\n\t'.join(fail_test_names)
        else:
            fail_test_name_str = 'Fail testcase: None'

        return f"""
        \n- Test Edit Time Of Quiz (Level 1) --\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """
    
    def run(self):
        self.setup_method(None)
        result = self.test(data)
        self.teardown_method(None)
        return result
    
    
        
with open('./input_editQuizTime.json', encoding='UTF-8') as f:
    data = json.load(f)
    test_data = [test_case['test_data'] for test_case in data]
    test_TestEditQuizTime_DataDriven = TestEditQuizTime(test_data)
    print(test_TestEditQuizTime_DataDriven.run())
  


  
