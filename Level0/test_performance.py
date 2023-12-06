from concurrent.futures import ThreadPoolExecutor, wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse

parser = argparse.ArgumentParser(description='Stress test the Python Selenium WebDriver')
parser.add_argument('--num', type=int, help='Number of simultaneous instances', default=20)
args = parser.parse_args()


class PerformanceTask:
    def __init__(self):
        self.driver = None

    def _setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

    def _teardown_method(self):
        if self.driver:
            self.driver.quit()

    def _precondition(self):
        pass

    def _logout(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

    def run_task(self):
        pass


class LoginTask(PerformanceTask):
    def __init__(self):
        super().__init__()
        
    def precondtion(self):
      self.driver.get("https://sandbox.moodledemo.net/")
      self.driver.set_window_size(787, 816)
      self.driver.find_element(By.LINK_TEXT, "Log in").click()
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").clear()
      self.driver.find_element(By.ID, "username").send_keys("teacher")
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "password").send_keys("sandbox")
      self.driver.find_element(By.ID, "loginbtn").click()
      
    def _task(self):
        try:
            self.precondtion()
            self._logout()
            return True
        except Exception as e:
            print(f"Exception in task: {e}")
        finally:
            self._teardown_method()
        return False

    def run_task(self):
        try:
            self._setup_method()
            return self._task()
        except Exception as e:
            self._teardown_method()
            raise e
    
class PerformanceRunner:
    def __init__(self, num_workers):
        self.__num_workers = num_workers

    def run(self, task_class):
        try:
            tasks = [task_class() for _ in range(self.__num_workers)]
            with ThreadPoolExecutor(max_workers=self.__num_workers) as executor:
                futures = [executor.submit(task.run_task) for task in tasks]
            wait(futures)
            success = 0
            failure = 0
            for idx, f in enumerate(futures):
                print(f'Result{idx}: {f.result()}, Error: {f.exception()}')
                success += 1 if f.result() else 0
                failure += 1 if f.exception() or not f.result() else 0
            print(f"""=======Run Succesfully with======== 
    Success: {success}, Failure: {failure}
    Error rate: {failure/(success+failure)}   
                """)
            return futures, success, failure
        except Exception as e:
            print(f"Exception in thread execution: {e}")


num = args.num
PerformanceRunner(num).run(LoginTask)
