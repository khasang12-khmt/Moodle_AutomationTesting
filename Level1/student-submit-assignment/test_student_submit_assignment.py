import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os
import json

MOODLE_URL = "https://sandbox400.moodledemo.net/"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "sandbox"
MAX_TIMEOUT_SHORT = 3
MAX_TIMEOUT = 10
MAX_TIMEOUT_LONG = 30
INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.json")

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
    driver.implicitly_wait(MAX_TIMEOUT_SHORT)
    driver.get("{}course/view.php?id=2".format(MOODLE_URL))
    try:
        driver.find_element(By.XPATH, "//button[contains(.,'Got it')]").click()
    except:
        pass
    driver.find_element(By.LINK_TEXT, "Assignment 1").click()
    try:
        driver.find_element(By.XPATH, "//button[contains(.,'Remove submission')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
    except:
        pass
    driver.find_element(By.LINK_TEXT, "My first course").click()

    yield driver

def get_input_data():
    with open(INPUT_PATH, "r", encoding='UTF-8') as f:
        data = json.load(f)
    return data

@pytest.mark.usefixtures("student_login", "delete_all_submissions")
class TestStudentSubmitAssignment:
    """
    Pre-condition:
        1. "My first course" exists
        2. "Assignment 1" exists
    """


    @pytest.mark.parametrize("assignmentName,isOverDue,files,method,specialCheck,expected", get_input_data())
    @pytest.mark.usefixtures("student_login", "delete_all_submissions")
    def test_file_submission(self, delete_all_submissions, assignmentName, isOverDue, files, method, specialCheck, expected):
        """
        Test case:
            Student submits an assignment
        """
        driver = delete_all_submissions
        print("Test case: Student submits an assignment")
        print("Assignment name: {}".format(assignmentName))
        