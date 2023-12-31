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

class TestCreateEvent():
    def __init__(self, data):
        self.data = data
        self.first_run = True

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()

    def precondition(self):
        self.driver.get("https://sandbox.moodledemo.net/")
        self.driver.set_window_size(926, 804)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("sandbox")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Calendar").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'New event\')]").click()
        time.sleep(3)
  
    def logout(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(3)

    def test_createEvent(self, name: str, startDay: str or None, startMonth: str or None, endDay: str or None, endMonth: str or None, endYear: str or None, error:str or None):
        try:
            self.precondition()
            self.driver.find_element(By.ID, "id_name").click()
            self.driver.find_element(By.ID, "id_name").clear()
            self.driver.find_element(By.ID, "id_name").send_keys(name)
            if startDay is not None:
                self.driver.find_element(By.ID, "id_timestart_day").click()
                self.driver.find_element(By.ID, "id_timestart_day").send_keys(startDay)
            if startMonth is not None:
                self.driver.find_element(By.ID, "id_timestart_month").click()
                self.driver.find_element(By.ID, "id_timestart_month").send_keys(startMonth)
            if endDay is not None:
                self.driver.find_element(By.XPATH, "//a[contains(.,\'Show more...\')]").click()
                if not self.driver.find_element(By.ID, "id_duration_1").is_selected():
                    self.driver.find_element(By.ID, "id_duration_1").click()
                self.driver.find_element(By.ID, "id_timedurationuntil_day").click()
                self.driver.find_element(By.ID, "id_timedurationuntil_day").send_keys(endDay)
            if endMonth is not None:
                self.driver.find_element(By.ID, "id_timedurationuntil_month").click()
                self.driver.find_element(By.ID, "id_timedurationuntil_month").send_keys(endMonth)
            if endYear is not None:
                self.driver.find_element(By.ID, "id_timedurationuntil_year").click()
                self.driver.find_element(By.ID, "id_timedurationuntil_year").send_keys(endYear)
            self.driver.find_element(By.XPATH, "//button[contains(.,\'Save\')]").click()
            time.sleep(3)
            if error is not None:
                if self.driver.find_element(By.ID, error) is None:
                    self.logout()
                    return False
                self.driver.find_element(By.XPATH, "//div[5]/div[2]/div/div/div/button/span").click()
            self.logout()
            return True
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.logout()
            return False

    def test(self, test_dict: dict):
        result = []
        for name, test in test_dict.items():
            print(name)
            result.append(self.test_createEvent(test["name"], test["startDay"], test["startMonth"], test["endDay"], test["endMonth"], test["endYear"], test["error"]))
        fail_test_name = []
        for i in range(0, len(result)):
            if not result[i]:
                fail_test_name.append(list(test_dict.keys())[i])

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        return f"""
        \n- Test Create Event (Level 1) --\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """
        
    def run(self):
        self.setup_method(None)
        result = self.test(data)
        self.teardown_method(None)
        return result

with open('./input/input_CreateEvent.json', encoding='UTF-8') as f:
    data = json.load(f)
    test_CreateEvent_DataDriven = TestCreateEvent(data)
    print(test_CreateEvent_DataDriven.run())