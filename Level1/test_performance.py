import argparse
import json
from PerformanceTask import PerformanceRunner as Runner
from PerformanceTask import Task

parser = argparse.ArgumentParser(description='Stress test the Python Selenium WebDriver')
parser.add_argument('--num', type=int, help='Number of simultaneous instances', default=20)
args = parser.parse_args()

class TestPerformance:
    def __init__(self):
        self.runner = Runner.PerformanceRunner()
       
    def test_Performance8(self):
        runner = Runner.PerformanceRunner(5)
        runner.stable_pattern(task_class=Task.UploadImageTask, stable_count=2, image_path='..\\testdata\\vinh\\big_image_10MB.png')
    
    def run(self, data):
        for testcase in data:
            workers = testcase["workers"]
            method_name = testcase["method"]
            stable_count = testcase["stable_count"]
            task_class = testcase["task_name"]
            kwargs = testcase["args"]
            
            self.runner.setWorker(workers)
            getattr(self.runner, method_name)(task_class=getattr(Task, task_class), stable_count=stable_count, **kwargs)

with open('./input/input_testPerformance.json') as f:
    data = json.load(f)
    
TestPerformance().run(data)