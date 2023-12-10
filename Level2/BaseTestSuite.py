from selenium import webdriver
from utils import TestDataParser
from TestDriverController import TestDriverController

class BaseTestSuite():  
  def __init__(self, data_path):
    self.first_run = True
    self.data = TestDataParser.parse_json(data_path)
    
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    TestDriverController.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    TestDriverController.driver.quit()
    
  def run_precondition(self, pre_condition):
    raise NotImplementedError()