import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver

class TestDataParser:
    @staticmethod
    def parse_json(json_file):
        with open(json_file, 'r') as file:
            test_data = json.load(file)
        return test_data


class TestUserCourse():
    def __init__(self, json_path):
        self.json_path = json_path
        self.first_run = True
    
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
    
    def run_precondition(self, pre_condition):
        test_items = pre_condition['test_items']
        for test_item in test_items:
            self.perform_test(test_item)

    def perform_test(self, test_item):
        try:
            element_type = test_item['element_type']
            element_locator = test_item['element_locator']
            action = test_item['action']
            value = test_item['value']

            if action == 'click':
                self.driver.find_element(element_type, element_locator).click()
            elif action == 'input':
                self.driver.find_element(element_type, element_locator).send_keys(value)
            elif action == 'select':
                dropdown = self.driver.find_element(element_type, element_locator)
                select = Select(dropdown)
                select.select_by_value(value)
            elif action == 'text_check':
                actual_text = self.driver.find_element(element_type, element_locator).text
                return actual_text == value
            elif action == 'sleep':
                time.sleep(value)

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return False

    def execute_test_data(self, test_data):
        result = []
        for scenario in list(test_data.values())[2:]:
            url = scenario['url']
            test_items = scenario['test_items']

            # Initialize setup
            self.driver.get(url)
            self.driver.set_window_size(784, 816)
            if self.first_run:
                self.first_run = False
                self.run_precondition(list(test_data.values())[0])
            else:
                self.run_precondition(list(test_data.values())[1])
                
            flag = False
            for test_item in test_items:
                res = self.perform_test(test_item)
                if res is True: flag = True
            result.append(flag)
        
        fail_test_name = []
        for i in range(0, len(result)):
            if not result[i]:
                fail_test_name.append(list(test_data.keys())[i])

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        return f"""
        \n- Test Add User To Course (Level 2) --\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """

    def run(self):
        test_data = TestDataParser.parse_json(self.json_path)
        self.setup_method(None)
        result = self.execute_test_data(test_data)
        self.teardown_method(None)
        return result

print(TestUserCourse("./input/input_UserCourse.json").run())