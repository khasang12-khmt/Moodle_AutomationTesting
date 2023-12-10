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
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("sandbox")
        self.driver.find_element(By.ID, "loginbtn").click()
        self.driver.find_element(By.LINK_TEXT, "My courses").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//span[3]").click()
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
  
    def logout(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(3)

    def test_updateCourse(self, fullname: str or NotImplemented, shortname: str, startDay: str or None, startMonth: str or None, startYear: str or None, endDay: str or None, endMonth: str or None, endYear: str or None, summary: str or None, file: str or None, category: str or None, error:str or None):
        try:
            self.precondition()
            if fullname is not None:
                self.driver.find_element(By.ID, "id_fullname").click()
                self.driver.find_element(By.ID, "id_fullname").clear()
                self.driver.find_element(By.ID, "id_fullname").send_keys(fullname)
            if shortname is not None:
                self.driver.find_element(By.ID, "id_shortname").click()
                self.driver.find_element(By.ID, "id_shortname").clear()
                self.driver.find_element(By.ID, "id_shortname").send_keys(shortname)
            if startDay is not None:
                self.driver.find_element(By.ID, "id_startdate_day").click()
                self.driver.find_element(By.ID, "id_startdate_day").send_keys(startDay)
            if startMonth is not None:
                self.driver.find_element(By.ID, "id_startdate_month").click()
                self.driver.find_element(By.ID, "id_startdate_month").send_keys(startMonth)
            if startYear is not None:
                self.driver.find_element(By.ID, "id_startdate_year").click()
                self.driver.find_element(By.ID, "id_startdate_year").send_keys(startYear)
            if endDay is not None:
                if not self.driver.find_element(By.ID, "id_enddate_enabled").is_selected():
                    self.driver.find_element(By.ID, "id_enddate_enabled").click()
                    time.sleep(1)
                self.driver.find_element(By.ID, "id_enddate_day").click()
                self.driver.find_element(By.ID, "id_enddate_day").send_keys(endDay)
            if endMonth is not None:
                self.driver.find_element(By.ID, "id_enddate_month").click()
                self.driver.find_element(By.ID, "id_enddate_month").send_keys(endMonth)
            if endYear is not None:
                self.driver.find_element(By.ID, "id_enddate_year").click()
                self.driver.find_element(By.ID, "id_enddate_year").send_keys(endYear)
            if summary is not None:
                self.driver.switch_to.frame(0)
                self.driver.find_element(By.CSS_SELECTOR, "p").click()
                element = self.driver.find_element(By.ID, "tinymce")
                self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>" + summary + "</p>'}", element)
                self.driver.switch_to.default_content()
                time.sleep(3)
            # if file is not None:
            #     self.driver.find_element(By.CSS_SELECTOR, ".fa-file-o").click()
            #     self.driver.find_element(By.NAME, "repo_upload_file").click()
            #     self.driver.find_element(By.NAME, "repo_upload_file").send_keys(file)
            #     self.driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
            if category is not None:
                if category != "":
                    self.driver.find_element(By.XPATH, "//div[2]/span/span").click()
                    self.driver.find_element(By.XPATH, "//span[contains(.,\'▼\')]").click()
                    self.driver.find_element(By.XPATH, "//li[contains(.,\'Miscellaneous\')]").click()
                else:
                    self.driver.find_element(By.XPATH, "//div[2]/span/span").click()
            self.driver.find_element(By.ID, "id_saveanddisplay").click()
            time.sleep(3)
            if error is not None:
                if self.driver.find_element(By.ID, error) is None:
                    self.logout()
                    return False
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
            result.append(self.test_updateCourse(test["fullname"],test["shortname"],  test["startDay"], test["startMonth"], test["startYear"], test["endDay"], test["endMonth"], test["endYear"], test["summary"], test["file"], test["category"], test["error"]))
        fail_test_name = []
        for i in range(0, len(result)):
            if not result[i]:
                fail_test_name.append(list(test_dict.keys())[i])

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        return f"""
        \n- Test Update Course (Level 1) --\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """
        
    def run(self):
        self.setup_method(None)
        result = self.test(data)
        self.teardown_method(None)
        return result

with open('./input/input_UpdateCourse.json', encoding='UTF-8') as f:
    data = json.load(f)
    test_updateCourse_DataDriven = TestCreateEvent(data)
    print(test_updateCourse_DataDriven.run())