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
MAX_TIMEOUT = 20
MAX_TIMEOUT_LONG = 30
INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.json")
FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "Level0", "student-submit-assignment", "files")

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
    return [(d["id"], d["assignmentName"], d["files"], d["method"], d["specialCheck"], d["expected"]) for d in data]

@pytest.mark.usefixtures("student_login", "delete_all_submissions")
class TestStudentSubmitAssignment:
    """
    Pre-condition:
        1. "My first course" exists
        2. "Assignment 1" exists
    """


    @pytest.mark.parametrize("id,assignmentName,files,method,specialCheck,expected", get_input_data())
    def test_file_submission(self, delete_all_submissions, id, assignmentName, files, method, specialCheck, expected):
        """
        Test case:
            Student submits an assignment
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT_LONG)
        driver.find_element(By.LINK_TEXT, assignmentName).click()

        # Special check logic before uploading files (if any)
        if specialCheck == "overdue":
            try:
                driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]")
                assert False
            except NoSuchElementException:
                assert True
            except Exception as e:
                print(e)
                assert False
            finally:
                return

        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        try:
            for file in files:
                # Upload file one by one
                wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
                wait.until(lambda d : d.find_element(By.XPATH, "//*[@title=\"Add...\"]").click() or True)

                if method == "file-picker::upload":
                    # Upload using "Upload a file" in file picker
                    driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
                    upload_file = os.path.abspath(os.path.join(FILE_PATH, file))
                    file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                    try:
                        file_input.send_keys(upload_file)
                        driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
                    except StaleElementReferenceException:
                        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                        file_input.send_keys(upload_file)
                        driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
                else:
                    # Upload by choosing from "Recent files" in file picker
                    driver.find_element(By.XPATH, "//span[contains(.,'Recent files')]").click()
                    driver.find_element(By.XPATH, "//p[contains(.,'{}')]".format(file)).click()
                    driver.find_element(By.XPATH, "//button[contains(.,'Select this file')]").click()
            
            # Special check logic after uploading files (if any)
            if specialCheck == "cannot_add":
                try:
                    driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
                    assert False
                except ElementNotInteractableException:
                    assert True
                except NoSuchElementException:
                    assert True
                except ElementClickInterceptedException:
                    assert True
                except Exception as e:
                    print(e)
                    assert False
                finally:
                    driver.find_element(By.NAME, "cancel").click()
                    return
            elif specialCheck is None:
                wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
                wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

                assert driver.find_element(By.XPATH, expected).is_displayed()
        
        except UnexpectedAlertPresentException:
            # Handle alert
            driver.switch_to.alert.accept()
            if specialCheck == "alert":
                assert True
                return
            assert False
        except Exception as e:
            # Handle other exceptions
            print(e)
            assert False
        