import argparse
import json
from PerformanceTask import PerformanceRunner as Runner
from PerformanceTask import Task
import logging
logging.basicConfig(filename='stress_test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestStress:
    def __init__(self):
        self.runner = Runner.PerformanceRunner()
       
    def run(self, data):
        for idx,testcase in enumerate(data):
            workers = testcase["workers"]
            method_name = testcase["method"]
            stable_count = testcase["stable_count"]
            task_class = testcase["task_name"]
            kwargs = testcase["args"]
            logging.info(f"++++ Running {idx+1} ++++")
            self.runner.setWorker(workers)
            getattr(self.runner, method_name)(task_class=getattr(Task, task_class), stable_count=stable_count, **kwargs)

with open('./input/input_testStress.json') as f:
    data = json.load(f)
    
TestStress().run(data)