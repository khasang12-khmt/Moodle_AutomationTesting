import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import os

MOODLE_URL = "https://sandbox400.moodledemo.net/"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "sandbox"

@pytest.fixture(scope="class")
def student_login():
    # Initialize a webdriver and log in a student
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MOODLE_URL)
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "username").send_keys(STUDENT_USERNAME)
    driver.find_element(By.ID, "password").send_keys(STUDENT_PASSWORD)
    driver.find_element(By.ID, "loginbtn").click()

    yield driver  # This will return the driver to the test
    # Teardown actions go here
    driver.quit()

@pytest.fixture(scope="function")
def delete_all_submissions(student_login):
    # Remove previous submissions (if any)
    driver = student_login
    driver.find_element(By.LINK_TEXT, "Home").click()
    driver.find_element(By.LINK_TEXT, "My first course").click()
    try:
        driver.find_element(By.XPATH, "//button[contains(.,'Got it')]").click()
    except:
        pass
    try:
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Remove submission')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
    except:
        pass
    driver.find_element(By.LINK_TEXT, "My first course").click()

    yield driver

@pytest.mark.usefixtures("student_login", "delete_all_submissions")
class TestStudentSubmitAssignment:
    def test_file_submission_1(self, delete_all_submissions):
        """
        Submit file assignment with 5 files (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(10)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        for i in range(5):
            # Upload file one by one
            driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "{}.txt".format(i+1)))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        driver.find_element(By.ID, "id_submitbutton").click()

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    def test_file_submission_2(self, delete_all_submissions):
        """
        Submit file assignment with 1 file (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(10)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "1.txt"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        driver.find_element(By.ID, "id_submitbutton").click()

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()