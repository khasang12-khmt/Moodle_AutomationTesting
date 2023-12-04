import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

MOODLE_URL = "https://sandbox400.moodledemo.net/"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "sandbox"

@pytest.fixture(scope="class")
def student_login():
    # Initialize a webdriver and log in a student
    driver = webdriver.Chrome()
    driver.get(MOODLE_URL)
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "username").send_keys(STUDENT_USERNAME)
    driver.find_element(By.ID, "password").send_keys(STUDENT_PASSWORD)
    driver.find_element(By.ID, "loginbtn").click()

    yield driver  # This will return the driver to the test
    # Teardown actions go here
    driver.quit()

@pytest.fixture(scope="class")
def delete_all_submissions(student_login):
    # Remove previous submissions (if any)
    driver = student_login
    driver.find_element(By.LINK_TEXT, "Home").click()
    driver.find_element(By.LINK_TEXT, "My first course").click()
    driver.find_element(By.LINK_TEXT, "Assignment 1").click()
    try:
        driver.find_element(By.XPATH, "//button[contains(.,'Remove submission')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(3)
    except:
        pass
    driver.find_element(By.LINK_TEXT, "My first course").click()

    yield driver

@pytest.mark.usefixtures("student_login", "delete_all_submissions")
class TestStudentSubmitAssignment:
    def test_file_submission_1(self, delete_all_submissions):
        """
        Submit file assignment with normal N, S
        """
        driver = delete_all_submissions
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        assert driver.find_element(By.ID, "id_submitbutton").is_displayed()