from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class TestDriverController:
    driver = None
    
    @staticmethod
    def perform_test(test_item):
        try:
            element_type = test_item['element_type']
            element_locator = test_item['element_locator']
            action = test_item['action']
            value = test_item['value']

            if action == 'click':
                TestDriverController.driver.find_element(element_type, element_locator).click()
            elif action == 'input':
                TestDriverController.driver.find_element(element_type, element_locator).send_keys(value)
            elif action == 'select':
                dropdown = TestDriverController.driver.find_element(element_type, element_locator)
                select = Select(dropdown)
                select.select_by_value(value)
            elif action == 'text_check':
                actual_text = TestDriverController.driver.find_element(element_type, element_locator).text
                return actual_text == value
            elif action == 'input_script':
                element = TestDriverController.driver.find_element(element_type, element_locator)
                TestDriverController.driver.execute_script(value, element)
            elif action == 'switch_to_default_content':
                TestDriverController.driver.switch_to.default_content()
            elif action == 'wait_frame':
                WebDriverWait(TestDriverController.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(value))
            elif action == 'wait_element':
                WebDriverWait(TestDriverController.driver, 10).until(expected_conditions.presence_of_element_located((element_type, element_locator))).click()
            elif action == 'sleep':
                time.sleep(value)
            elif action == 'assert_check':
                elements = TestDriverController.driver.find_elements(By.ID, element_locator)
                return len(elements) > 0
            elif action == 'get':
                TestDriverController.driver.get(value)
            elif action == 'set_window_size':
                width, height = map(int, value.split('x'))
                TestDriverController.driver.set_window_size(width, height)
            else:
                print(test_item)
                raise NotImplementedError()

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return False