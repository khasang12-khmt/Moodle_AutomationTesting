import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import os

MOODLE_URL = "https://sandbox400.moodledemo.net/"
TEACHER_USERNAME = "teacher"
TEACHER_PASSWORD = "sandbox"
MAX_TIMEOUT_SHORT = 3
MAX_TIMEOUT = 10
MAX_TIMEOUT_LONG = 600

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
def remove_uploaded_file(teacher_login):
    # Remove previous uploaded file (if any)
    driver = teacher_login
    driver.implicitly_wait(MAX_TIMEOUT_SHORT)
    driver.get("{}course/view.php?id=2".format(MOODLE_URL))
    if driver.find_element(By.NAME, "setmode").is_selected() == False:
        driver.find_element(By.NAME, "setmode").click()
    try:
        if driver.find_element(By.XPATH, "//a[contains(.,'New file')]").is_displayed():
            driver.find_element(By.XPATH, "//li[2]/div/div/div[2]/div/div/div/div/a/i").click()
            driver.find_element(By.XPATH, "//li[2]/div/div/div[2]/div/div/div/div/div/a[6]/span").click()
            driver.find_element(By.XPATH, "//button[contains(.,'Yes')]").click()
    except:
        pass

    yield driver

@pytest.mark.usefixtures("teacher_login", "remove_uploaded_file")
class TestTeacherUploadFile:
    """
    Pre-condition:
        1. "My first course" exists
    """

    
    def test_teacher_upload_file_1(self, remove_uploaded_file):
        """
        UF-ECP-001
        Upload a file with:
            - File name: "New file"
            - "1.txt" (no folder, valid file)
            - Display: embed
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")
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

        # Display: embed
        driver.find_element(By.XPATH, "//a[contains(.,'Appearance')]").click()
        select_display = Select(driver.find_element(By.ID, "id_display"))
        select_display.select_by_visible_text("Embed")

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.XPATH, "//a[contains(.,'New file')]").is_displayed()

    
    def test_teacher_upload_file_2(self, remove_uploaded_file):
        """
        UF-ECP-002
        Upload a file with:
            - File name: "New file"
            - "1.txt" (in folder, valid file)
            - Display: Force download
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")
        # Create a folder
        driver.find_element(By.XPATH, "//*[@title=\"Create folder\"]").click()
        driver.find_element(By.XPATH, "//input[contains(@id,'fm-newname')]").send_keys("New folder")
        driver.find_element(By.XPATH, "//button[contains(.,'Create folder')]").click()
        driver.find_element(By.XPATH, "//a[contains(.,'New folder')]").click()

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

        # Display: Force download
        driver.find_element(By.XPATH, "//a[contains(.,'Appearance')]").click()
        select_display = Select(driver.find_element(By.ID, "id_display"))
        select_display.select_by_visible_text("Force download")

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.XPATH, "//a[contains(.,'New file')]").is_displayed()

    
    def test_teacher_upload_file_3(self, remove_uploaded_file):
        """
        UF-ECP-003
        Upload a file with:
            - File name: "New file"
            - "1.txt" (no folder, valid file)
            - Display: Open
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")
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

        # Display: open
        driver.find_element(By.XPATH, "//a[contains(.,'Appearance')]").click()
        select_display = Select(driver.find_element(By.ID, "id_display"))
        select_display.select_by_visible_text("Open")

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.XPATH, "//a[contains(.,'New file')]").is_displayed()

    
    def test_teacher_upload_file_4(self, remove_uploaded_file):
        """
        UF-ECP-004
        Upload a file with (fail):
            - File name: empty
            - "1.txt" (no folder, valid file)
            - Display: Embed
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

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

        # Display: embed
        driver.find_element(By.XPATH, "//a[contains(.,'Appearance')]").click()
        select_display = Select(driver.find_element(By.ID, "id_display"))
        select_display.select_by_visible_text("Embed")

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.ID, "id_error_name").text == "- You must supply a value here."

    
    def test_teacher_upload_file_5(self, remove_uploaded_file):
        """
        UF-ECP-005
        Upload a file with (fail):
            - File name: "New file"
            - no file
            - Display: Embed
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")

        # Display: embed
        driver.find_element(By.XPATH, "//a[contains(.,'Appearance')]").click()
        select_display = Select(driver.find_element(By.ID, "id_display"))
        select_display.select_by_visible_text("Embed")

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.ID, "id_error_files").text == "Required"
    
    @pytest.mark.skip(reason="The upload process is too long")
    def test_teacher_upload_file_6(self, remove_uploaded_file):
        """
        UF-ECP-006
        Upload a file with (fail):
            - File name: "New file"
            - "1.mp4" (no folder, invalid file because of size > 256MB)
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT_LONG)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")
        # Upload one file
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

        assert driver.find_element(By.XPATH, "//span[contains(.,'The maximum size for a file is 256 MB')]").is_displayed()


    def test_teacher_upload_file_7(self, remove_uploaded_file):
        """
        UF-DT-001
        Upload file (all conditions are true)
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")
        # Create a folder
        driver.find_element(By.XPATH, "//*[@title=\"Create folder\"]").click()
        driver.find_element(By.XPATH, "//input[contains(@id,'fm-newname')]").send_keys("New folder")
        driver.find_element(By.XPATH, "//button[contains(.,'Create folder')]").click()
        driver.find_element(By.XPATH, "//a[contains(.,'New folder')]").click()

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

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.XPATH, "//a[contains(.,'New file')]").is_displayed()

    
    def test_teacher_upload_file_8(self, remove_uploaded_file):
        """
        UF-DT-002
        Upload file (not create folder)
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")
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

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.XPATH, "//a[contains(.,'New file')]").is_displayed()


    def test_teacher_upload_file_9(self, remove_uploaded_file):
        """
        UF-DT-003
        Upload file (not upload file)
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

        driver.find_element(By.ID, "id_name").send_keys("New file")

        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.ID, "id_error_files").text == "Required"


    def test_teacher_upload_file_10(self, remove_uploaded_file):
        """
        UF-DT-004
        Upload file (not input file name)
        """
        driver = remove_uploaded_file
        driver.implicitly_wait(MAX_TIMEOUT)
        driver.find_element(By.XPATH, "//span[contains(.,'Add an activity or resource')]").click()
        driver.find_element(By.XPATH, "//div[8]/div/a/div/img").click()

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


        driver.find_element(By.ID, "id_submitbutton2").click()

        assert driver.find_element(By.ID, "id_error_name").text == "- You must supply a value here."