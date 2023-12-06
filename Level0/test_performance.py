import argparse
from PerformanceTask import PerformanceRunner as Runner
from PerformanceTask import Task

parser = argparse.ArgumentParser(description='Stress test the Python Selenium WebDriver')
parser.add_argument('--num', type=int, help='Number of simultaneous instances', default=20)
args = parser.parse_args()

class TestPerformance:
       
    def test_Performance1(self):
        runner = Runner.PerformanceRunner(5)
        runner.stable_pattern(task_class=Task.GoToCourseTask, stable_count=10)
    
    def test_Performance2(self):
        runner = Runner.PerformanceRunner(5)
        runner.ramp_up_pattern(task_class=Task.GoToCourseTask, stable_count=2, step=2)

    def test_Performance3(self):
        runner = Runner.PerformanceRunner(10)
        runner.stable_pattern(task_class=Task.GoToCourseTask, stable_coksunt=10)
    
    def test_Performance4(self):
        runner = Runner.PerformanceRunner(10)
        runner.ramp_up_pattern(task_class=Task.GoToCourseTask, stable_count=2, step=2)
    
    def test_Performance3(self):
        runner = Runner.PerformanceRunner(20)
        runner.stable_pattern(task_class=Task.GoToCourseTask, stable_count=5)
    
    def test_Performance4(self):
        runner = Runner.PerformanceRunner(20)
        runner.ramp_up_pattern(task_class=Task.GoToCourseTask, stable_count=2, step=2)
        
    def test_Performance7(self):
        runner = Runner.PerformanceRunner(5)
        runner.stable_pattern(task_class=Task.UploadImageTask, stable_count=2, image_path='..\\testdata\\vinh\\image.png')
    
    def test_Performance8(self):
        runner = Runner.PerformanceRunner(10)
        runner.stable_patterns(task_class=Task.UploadImageTask, stable_count=2, image_path='..\\testdata\\vinh\\image.png')
        
    def test_Performance8(self):
        runner = Runner.PerformanceRunner(5)
        runner.stable_pattern(task_class=Task.UploadImageTask, stable_count=2, image_path='..\\testdata\\vinh\\big_image_10MB.png')
    
    def run(self):
        test_methods = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith("test_Performance")]
        test_methods = sorted(test_methods, key=lambda x: int(x.split('test_Performance')[1]))
        fs = list(map(lambda mname: getattr(self, mname), test_methods))
        for f in fs:
            f()

TestPerformance().run()
