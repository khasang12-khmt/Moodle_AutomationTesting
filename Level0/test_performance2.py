from concurrent.futures import ThreadPoolExecutor, wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse

parser = argparse.ArgumentParser(description='Stress test the Python Selenium WebDriver')
parser.add_argument('--num', type=int, help='Number of simultaneous instances', default=20)
parser.add_argument('--type', help='How to run the instances', choices=['parallel', 'concurrent'])
args = parser.parse_args()

def run():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.get("https://sandbox.moodledemo.net/")
        driver.set_window_size(787, 816)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").click()
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "password").send_keys("sandbox")
        driver.find_element(By.ID, "loginbtn").click()
        driver.close()
        driver.quit()
    except Exception as e:
        raise e

num = args.num
with ThreadPoolExecutor(max_workers=num) as executor:
    futures = [executor.submit(run) for _ in range(num)]

wait(futures)

for f in futures:
    print(f.exception())
