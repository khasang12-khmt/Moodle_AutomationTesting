# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestResponsive():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_responsive1(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(1920, 1080)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
      self.driver.find_element(By.ID, "username").send_keys("")
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("teacher")
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive2(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(1366, 768)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive3(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(1280, 720)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive4(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(1280, 1024)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive5(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(1440, 900)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive6(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(360, 800)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
      time.sleep(3)
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"   

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click(  )
        self.driver.find_element(By.LINK_TEXT, "Log out").click() 
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive7(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(390, 844)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
      time.sleep(3)
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"   

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click(  )
        self.driver.find_element(By.LINK_TEXT, "Log out").click() 
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive8(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(414, 896)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
      time.sleep(3)
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"   

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click(  )
        self.driver.find_element(By.LINK_TEXT, "Log out").click() 
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive9(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(393, 873)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
      time.sleep(3)
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"   

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click(  )
        self.driver.find_element(By.LINK_TEXT, "Log out").click() 
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
  
  def test_responsive10(self):
    try:
      self.driver.get("https://school.moodledemo.net/")
      self.driver.set_window_size(412, 915)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "password").send_keys("moodle")
      self.driver.find_element(By.ID, "loginbtn").click()
      self.driver.find_element(By.ID, "page-header").click()
      flag1 = self.driver.find_element(By.ID, "instance-472-header").text == "Course overview"
      self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
      time.sleep(3)
      self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
      flag2 = self.driver.find_element(By.CSS_SELECTOR, ".h2").text == "Dashboard"   

      if (flag1 and flag2) is True:
        self.driver.find_element(By.ID, "user-menu-toggle").click(  )
        self.driver.find_element(By.LINK_TEXT, "Log out").click() 
        return True
      else: 
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
      return False
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
    \n- Test Responsiveness (Level 0)--\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
    """
    
  def run(self):

    self.setup_method(None)

    result = self.test(
      self.test_responsive1,
      self.test_responsive2,
      self.test_responsive3,
      self.test_responsive4,
      self.test_responsive5,
      self.test_responsive6,
      self.test_responsive7,
      self.test_responsive8,
      self.test_responsive9,
      self.test_responsive10
    )

    self.teardown_method(None)

    return result
  
responsive = TestResponsive()
print(responsive.run())