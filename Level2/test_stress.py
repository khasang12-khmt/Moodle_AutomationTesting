import json
from selenium import webdriver
from PerformanceTask import Task
from PerformanceTask import PerformanceRunner as Runner
import logging
logging.basicConfig(filename='stress_test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestDataParser:
    @staticmethod
    def parse_json(json_file):
        with open(json_file, 'r') as file:
            test_data = json.load(file)
        return test_data

class TestStress():
      
    def __init__(self,data):
        self.data = data
        self.first_run = True
        self.runner = Runner.PerformanceRunner()
       
    def run(self):
        for idx,testcase in enumerate(self.data):
            url = testcase.get("url")
            tasks = testcase.get("tasks")
            
            workers = testcase.get("workers")
            method_name = testcase.get("method")
            stable_count = testcase.get("stable_count")
            task_class = testcase.get("task_class")

            kwargs = testcase.get("args") or {}
            
            self.runner.setWorker(workers)
            logging.info(f"++++ Running {idx+1} ++++")
            try:
                task_class = getattr(Task, task_class)
                getattr(self.runner, method_name)(task_class=task_class, stable_count=stable_count, **kwargs)
            except:
                kwargs["url"] = url
                kwargs["tasks"] = tasks
                getattr(self.runner, method_name)(task_class=Task.CustomTask, stable_count=stable_count, **kwargs)
    

TestStress(TestDataParser.parse_json('./input/input_testStress.json')).run()