import json
import json
from selenium import webdriver

from PerformanceTask import Task
class TestDataParser:
    @staticmethod
    def parse_json(json_file):
        with open(json_file, 'r') as file:
            test_data = json.load(file)
        return test_data

class TestProfileUpdate():
    def __init__(self,data):
        self.data = data
        self.executor = Task.Executor()
    
    def run(self):
        result = []
        for testcase in self.data:
            self.executor.url = testcase.get('url', '')
            self.executor.tasks = testcase.get('tasks', [])
            res = True or self.executor.run_task()
            print(f"Run testcase {testcase['id']}: {res}")
            result.append(res)
        
        fail_test_name = []
        for i in range(0, len(result)):
            if isinstance(result[i], Exception):
                err = result[i]
                fail_test_name.append(f"{self.data[i]['id']} {err=}")

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        return f"""
        \n- Test Profile Update (Level 2) --\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """
        
print(TestProfileUpdate(TestDataParser.parse_json('./input/input_profileUpdate.json')).run())