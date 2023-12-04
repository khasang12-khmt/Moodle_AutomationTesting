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

class TestCreateDiscussion():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_discussion1(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
      self.driver.find_element(By.ID, "username").send_keys("")
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("teacher")
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//span[3]").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("")
      time.sleep(3)
      
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      if self.driver.find_element(By.ID, "id_error_subject").text == "- Required":
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion2(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("a")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion3(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("ab")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion4(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion5(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion6(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      self.driver.find_element(By.ID, "id_error_subject").click()
      if self.driver.find_element(By.ID, "id_error_subject").text == "- Maximum of 255 characters":
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion7(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Hello World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion8(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p></p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      if self.driver.find_element(By.ID, "id_error_message").text == "- Required":
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False

  def test_discussion9(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>a</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion10(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>ab</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion11(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "#course-info-container-69-4 .multiline").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion12(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//span[3]").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>H World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_advancedadddiscussion").click()
      self.driver.find_element(By.ID, "collapseElement-2").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//div[3]/input").click()
      self.driver.find_element(By.XPATH, "//div[3]/input").send_keys("Intro")
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False     
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=} {err.with_traceback}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
      
  def test_discussion13(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//span[3]").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("Hello")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>H World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_advancedadddiscussion").click()
      self.driver.find_element(By.ID, "collapseElement-2").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//div[3]/input").click()
      self.driver.find_element(By.XPATH, "//div[3]/input").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False     
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion14(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//span[3]").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("ab")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>H World</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_advancedadddiscussion").click()
      self.driver.find_element(By.ID, "collapseElement-2").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//div[3]/input").click()
      self.driver.find_element(By.XPATH, "//div[3]/input").send_keys("")
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False     
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion15(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//span[3]").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("aabc")
      time.sleep(3)
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p></p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_advancedadddiscussion").click()
      self.driver.find_element(By.ID, "collapseElement-2").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//div[3]/input").click()
      self.driver.find_element(By.XPATH, "//div[3]/input").send_keys("Intro2")
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False     
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_discussion16(self):
    print(sys._getframe(0).f_code.co_name)
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(790, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//span[3]").click()
      self.driver.find_element(By.CSS_SELECTOR, "#module-967 .aalink").click()
      self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
      time.sleep(3)
      self.driver.find_element(By.ID, "id_subject").click()
      self.driver.find_element(By.ID, "id_subject").send_keys("")
      WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it("id_message_ifr"))
      element = self.driver.find_element(By.ID, "tinymce")
      self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Xin chào</p>'}", element)
      self.driver.switch_to.default_content()
      self.driver.find_element(By.ID, "id_advancedadddiscussion").click()
      self.driver.find_element(By.ID, "collapseElement-2").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//div[3]/input").click()
      self.driver.find_element(By.XPATH, "//div[3]/input").send_keys("Intro3")
      self.driver.find_element(By.ID, "id_submitbutton").click()
      elements = self.driver.find_elements(By.ID, "user-notifications")
      if len(elements) > 0:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else:
        self.driver.find_element(By.ID, "action-menu-toggle-0").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False     
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "action-menu-toggle-0").click()
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
    \n- Test Create Discussion To Course (Level 0)--\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
    """
    
  def run(self):

    self.setup_method(None)

    result = self.test(
      self.test_discussion1,
      self.test_discussion2,
      self.test_discussion3,
      self.test_discussion4,
      self.test_discussion5,
      self.test_discussion6,
      self.test_discussion7,
      self.test_discussion8,
      self.test_discussion9,
      self.test_discussion10,
      self.test_discussion11,
      self.test_discussion12,
      self.test_discussion13,
      self.test_discussion14,
      self.test_discussion15,
      self.test_discussion16
    )

    self.teardown_method(None)

    return result
  
createDiscussion = TestCreateDiscussion()
print(createDiscussion.run())