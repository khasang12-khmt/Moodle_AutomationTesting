import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import os
import json

MOODLE_URL = "https://sandbox400.moodledemo.net/"
TEACHER_USERNAME = "teacher"
TEACHER_PASSWORD = "sandbox"
MAX_TIMEOUT_SHORT = 3
MAX_TIMEOUT = 10
MAX_TIMEOUT_LONG = 600
INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.json")
FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "Level0", "teacher-upload-file", "files")

@pytest.fixture(scope="class")
def teacher_login():
    # Initialize a webdriver and log in a teacher
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MOODLE_URL)
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "username").send_keys(TEACHER_USERNAME)
    driver.find_element(By.ID, "password").send_keys(TEACHER_PASSWORD)
    driver.find_element(By.ID, "loginbtn").click()

    yield driver  # This will return the driver to the test
    # Teardown actions go here
    driver.quit()

@pytest.fixture(scope="function")
def remove_uploaded_file(teacher_login, id, fileName, **kwargs):
    # Remove previous uploaded file (if any)
    driver = teacher_login
    driver.implicitly_wait(MAX_TIMEOUT_SHORT)
    driver.get("{}course/view.php?id=2".format(MOODLE_URL))
    if driver.find_element(By.NAME, "setmode").is_selected() == False:
        driver.find_element(By.NAME, "setmode").click()
    try:
        if driver.find_element(By.XPATH, "//a[contains(.,'{}')]".format(fileName)).is_displayed():
            driver.find_element(By.XPATH, "//li[2]/div/div/div[2]/div/div/div/div/a/i").click()
            driver.find_element(By.XPATH, "//li[2]/div/div/div[2]/div/div/div/div/div/a[6]/span").click()
            driver.find_element(By.XPATH, "//button[contains(.,'Yes')]").click()
    except:
        pass

    yield driver

def get_input_data():
    with open(INPUT_PATH, "r", encoding='UTF-8') as f:
        data = json.load(f)
    return [(d["id"], d["fileName"], d["file"], d["directory"], d["display"], d["specialCheck"], d["expected"]) for d in data]

@pytest.mark.usefixtures("teacher_login", "remove_uploaded_file")
class TestTeacherUploadFile:
    """
    Pre-condition:
        1. "My first course" exists
    """


    @pytest.mark.parametrize("id,fileName,file,directory,display,specialCheck,expected", get_input_data())
    def test_teacher_upload_file(self, remove_uploaded_file, id, fileName, file, directory, display, specialCheck, expected):
        """
        Test case:
            Teacher uploads a file to a course
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click() or True)
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        if fileName != "":
            driver.find_element(By.ID, "id_name").send_keys(fileName)

        if file != "":
            if directory != "":
                # Create a folder
                driver.find_element(By.XPATH, "//*[@title=\"Create folder\"]").click()
                driver.find_element(By.XPATH, "//input[contains(@id,'fm-newname')]").send_keys(directory)
                driver.find_element(By.XPATH, "//button[contains(.,'Create folder')]").click()
                driver.find_element(By.XPATH, "//a[contains(.,'{}')]".format(directory)).click()

            # Upload one file
            driver.find_element(By.XPATH, "//*[@title=\"Add...\"]").click()
            driver.find_element(By.XPATH, "//span[contains(.,'Upload a file')]").click()
            upload_file = os.path.abspath(os.path.join(FILE_PATH, "1.txt"))
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            try:
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()
            except StaleElementReferenceException:
                file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                file_input.send_keys(upload_file)
                driver.find_element(By.XPATH, "//button[contains(.,'Upload this file')]").click()

        if display != "":
            # Set display
            wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
            wait.until(lambda d : d.find_element(By.XPATH, "//a[contains(.,'Appearance')]").click() or True)
            select_display = Select(driver.find_element(By.ID, "id_display"))
            select_display.select_by_visible_text(display)

        if specialCheck == "file_too_large":
            assert driver.find_element(By.XPATH, "//span[contains(.,'The maximum size for a file is 256 MB')]").is_displayed()
            return

        wait = WebDriverWait(driver, timeout=MAX_TIMEOUT, poll_frequency=0.5, ignored_exceptions=ElementClickInterceptedException)
        wait.until(lambda d : d.find_element(By.ID, "id_submitbutton2").click() or True)

        if specialCheck == "no_name":
            assert driver.find_element(By.ID, "id_error_name").text == "- You must supply a value here."
            return
        if specialCheck == "no_file":
            assert driver.find_element(By.ID, "id_error_files").text == "Required"
            return
        assert driver.find_element(By.XPATH, expected).is_displayed()