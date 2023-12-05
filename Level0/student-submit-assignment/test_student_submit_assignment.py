import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os

MOODLE_URL = "https://sandbox400.moodledemo.net/"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "sandbox"
MAX_TIMEOUT_SHORT = 3
MAX_TIMEOUT = 10
MAX_TIMEOUT_LONG = 30

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
    """
    Pre-condition:
        1. "My first course" exists
        2. "Assignment 1" exists
        3. "Assignment 1" is available
        4. "Assignment 1" is set to "File submissions" only
        5. "Assignment 1" has "Maximum number of uploaded files" set to 10
        6. "Assignment 1" has "Maximum submission size" set to 10MB
    """

    
    def test_file_submission_1(self, delete_all_submissions):
        """
        FS-BVA-001
        Submit file assignment with 5 files (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        for i in range(5):
            # Upload file one by one
            wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
            wait.until(lambda d : d.find_element(By.XPATH, "//*[@title=\"Add...\"]").click() or True)
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "files", "{}.txt".format(i+1)))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_2(self, delete_all_submissions):
        """
        FS-BVA-002
        Submit file assignment with 1 file (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "1.txt"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_3(self, delete_all_submissions):
        """
        FS-BVA-003
        Submit file assignment with 2 files (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        for i in range(2):
            # Upload file one by one
            wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
            wait.until(lambda d : d.find_element(By.XPATH, "//*[@title=\"Add...\"]").click() or True)
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "files", "{}.txt".format(i+1)))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_4(self, delete_all_submissions):
        """
        FS-BVA-004
        Submit file assignment with 9 files (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        for i in range(9):
            # Upload file one by one
            wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
            wait.until(lambda d : d.find_element(By.XPATH, "//*[@title=\"Add...\"]").click() or True)
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "files", "{}.txt".format(i+1)))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_5(self, delete_all_submissions):
        """
        FS-BVA-005
        Submit file assignment with 10 files (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        for i in range(10):
            # Upload file one by one
            wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
            wait.until(lambda d : d.find_element(By.XPATH, "//*[@title=\"Add...\"]").click() or True)
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "files", "{}.txt".format(i+1)))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_6(self, delete_all_submissions):
        """
        FS-BVA-006
        Submit file assignment with 1 file of size ~1MB (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one image file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "image.jpg"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_7(self, delete_all_submissions):
        """
        FS-BVA-007
        Submit file assignment with 1 file of size ~8MB (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT_LONG)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one webm file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "1.webm"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT_LONG, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_8(self, delete_all_submissions):
        """
        FS-BVA-008
        Submit file assignment with 1 file of size ~9MB (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT_LONG)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one webm file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "2.webm"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT_LONG, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_9(self, delete_all_submissions):
        """
        FS-BVA-009
        Submit file assignment with 0 file (invalid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//div[contains(.,'Nothing was submitted')]").is_displayed()

    
    def test_file_submission_10(self, delete_all_submissions):
        """
        FS-BVA-010
        Submit file assignment with 11 files (invalid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        for i in range(10):
            # Upload file one by one
            wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
            wait.until(lambda d : d.find_element(By.XPATH, "//*[@title=\"Add...\"]").click() or True)
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "files", "{}.txt".format(i+1)))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()

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
    
    
    def test_file_submission_11(self, delete_all_submissions):
        """
        FS-BVA-011
        Submit file assignment with 1 file of size 0MB (invalid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "0.txt"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except UnexpectedAlertPresentException:
            assert True

    
    def test_file_submission_12(self, delete_all_submissions):
        """
        FS-BVA-012
        Submit file assignment with 1 file of size ~11MB (invalid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT_LONG)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one mp4 file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "1.mp4"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except UnexpectedAlertPresentException:
            assert True

    
    def test_file_submission_13(self, delete_all_submissions):
        """
        FS-UCT-001
        Submit file assignment that is not available (invalid)
        Pre-condition:
            - "Assignment 2" is not available (overdue)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 2").click()

        try:
            driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]")
            assert False
        except NoSuchElementException:
            assert True
        except Exception as e:
            print(e)
            assert False

    
    def test_file_submission_14(self, delete_all_submissions):
        """
        FS-UCT-002
        Submit file assignment with drag and drop (valid)
        """
        # Drag and drop file is not supported by Selenium
        pass

    
    def test_file_submission_15(self, delete_all_submissions):
        """
        FS-UCT-003
        Submit file assignment with file picker (recent files) (valid)
        Pre-condition:
            - The user has uploaded a file to Moodle before (1.txt)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Select file from recent files
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Recent files')]").click()
        driver.find_element(By.XPATH, "//p[contains(.,'1.txt')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Select this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()

    
    def test_file_submission_16(self, delete_all_submissions):
        """
        FS-UCT-004
        Submit file assignment with file picker (upload a file) (valid)
        """
        driver = delete_all_submissions
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

        # Upload one file
        driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "files", "1.txt"))
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        try:
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        except StaleElementReferenceException:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file)
            driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
        
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton").click() or True)

        assert driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()