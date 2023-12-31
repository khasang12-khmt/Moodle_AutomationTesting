# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from BaseTestSuite import BaseTestSuite
from TestRunner import TestRunner

class TestUserCourseSuite(BaseTestSuite):
  def test_userCourse(self, test):
    try:
      email, cohort, role, helper_email, helper_cohort, expected = test["email"], test["cohort"], test["role"], test["helper_email"], test["helper_cohort"], test["expected"]
      # init setup
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(784, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      if self.first_run:
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.first_run = False
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.LINK_TEXT, "Participants").click()
      self.driver.find_element(By.CSS_SELECTOR, "#enrolusersbutton-1 .btn").click()
      time.sleep(3)
      
      # email
      self.driver.find_element(By.XPATH, "//div[3]/input").click()
      self.driver.execute_script("window.scrollTo(0,0)")
      self.driver.execute_script("window.scrollTo(0,0)")
      self.driver.find_element(By.XPATH, "//div[3]/input").send_keys(email)
      if helper_email == 1:
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/ul/li").click()
      
      # cohort
      self.driver.find_element(By.ID, "id_cohortlist_label").click()
      self.driver.find_element(By.XPATH, "//div[2]/div[2]/div[3]/input").send_keys(cohort)
      if helper_cohort == 1:
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/ul/li").click()
      
      # role
      if role != "":
        self.driver.find_element(By.ID, "id_roletoassign").click()
        dropdown = self.driver.find_element(By.ID, "id_roletoassign")
        select = Select(dropdown)
        select.select_by_value('4')
        
      # submit
      time.sleep(1)
      self.driver.find_element(By.XPATH, "//div[2]/div/div/div[3]/button[2]").click()
      time.sleep(3)
      self.driver.execute_script("window.scrollTo(0,400)")
      self.driver.find_element(By.XPATH, "//div[3]/table/tbody/tr/td[2]").click()
      self.driver.find_element(By.ID, "user-index-participants-69_r2").click()
      
      # expect
      if self.driver.find_element(By.CSS_SELECTOR, ".toast-message").text == expected: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True if expected == "0 enrolled users" else False
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False if expected == "0 enrolled users" else True
      
    except Exception as err: 
      print(f"Unexpected {err=}, {type(err)=}")
      return False

userCourseTestSuite = TestUserCourseSuite('./input/input_UserCourse.json')
TestRunner.run(userCourseTestSuite,"Add User To Course")