import argparse
from PerformanceTask import PerformanceRunner as Runner
from PerformanceTask import Task
import logging
logging.basicConfig(filename='stress_test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class TestStress:
    def test_Stress1(self):
        runner = Runner.PerformanceRunner(3)
        runner.stable_pattern(task_class=Task.GoToCourseTask, stable_count=10)
       
    def test_Stress2(self):
        runner = Runner.PerformanceRunner(5)
        runner.stable_pattern(task_class=Task.GoToCourseTask, stable_count=10)
        
    def test_Stress3(self):
        runner = Runner.PerformanceRunner(10)
        runner.stable_pattern(task_class=Task.GoToCourseTask, stable_count=10)
        
    def test_Stress4(self):
        runner = Runner.PerformanceRunner(3)
        runner.ramp_up_pattern(task_class=Task.GoToCourseTask, stable_count=5, step=2)
    
    def test_Stress5(self):
        runner = Runner.PerformanceRunner(5)
        runner.ramp_up_pattern(task_class=Task.GoToCourseTask, stable_count=5, step=2)
    
    def test_Stress6(self):
        runner = Runner.PerformanceRunner(10)
        runner.ramp_up_pattern(task_class=Task.GoToCourseTask, stable_count=5, step=2)
        
    def test_Stress7(self):
        runner = Runner.PerformanceRunner(5)
        runner.stable_pattern(task_class=Task.UploadImageTask, stable_count=2, image_path='..\\testdata\\vinh\\image.png')
    
    def test_Stress8(self):    
        runner = Runner.PerformanceRunner(10)
        runner.stable_pattern(task_class=Task.UploadImageTask, stable_count=2, image_path='..\\testdata\\vinh\\big_image_10MB.png')

    def test_Stress9(self):
        runner = Runner.PerformanceRunner(5)
        runner.ramp_up_pattern(task_class=Task.UploadImageTask, stable_count=5, image_path='..\\testdata\\vinh\\image.png')
    
    def test_Stress10(self):    
        runner = Runner.PerformanceRunner(10)
        runner.ramp_up_pattern(task_class=Task.UploadImageTask, stable_count=5, image_path='..\\testdata\\vinh\\big_image_10MB.png')

    def run(self):
        test_methods = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith("test_Stress")]
        test_methods = sorted(test_methods, key=lambda x: int(x.split('test_Stress')[1]))
        fs = list(map(lambda mname: getattr(self, mname), test_methods))
        for f in fs:
            logging.info(f"++++ Running {f.__name__} ++++")
            f()

TestStress().run()