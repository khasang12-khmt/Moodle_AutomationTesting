import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

MOODLE_URL = "https://sandbox400.moodledemo.net/"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "sandbox"
INCORRECT_STUDENT_USERNAME = "student1"
MAX_TIMEOUT = 3

@pytest.fixture(scope="class")
def set_up():
    # Initialize a webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(MAX_TIMEOUT)

    yield driver  # This will return the driver to the test
    # Teardown actions go here
    driver.quit()

@pytest.mark.usefixtures("set_up")
class TestAuthenticate:
    

    def test_view_course_without_login(self, set_up):
        driver = set_up
        driver.get("{}course/view.php?id=2".format(MOODLE_URL))

        # Assert true if the login form is displayed and the course is not displayed
        assert driver.find_element(By.CSS_SELECTOR, "form[id='login']").is_displayed() == True
        try:
            driver.find_element(By.XPATH, "//h1[contains(.,'My first course')]").is_displayed()
            assert False
        except NoSuchElementException:
            assert True

    def test_view_course_with_incorrect_login(self, set_up):
        driver = set_up
        driver.get(MOODLE_URL)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        # Log in a student (incorrect username)
        driver.find_element(By.ID, "username").send_keys(INCORRECT_STUDENT_USERNAME)
        driver.find_element(By.ID, "password").send_keys(STUDENT_PASSWORD)
        driver.find_element(By.ID, "loginbtn").click()

        driver.get("{}course/view.php?id=2".format(MOODLE_URL))
        # Assert true if the login form is displayed and the course is not displayed
        assert driver.find_element(By.CSS_SELECTOR, "form[id='login']").is_displayed() == True
        try:
            driver.find_element(By.XPATH, "//h1[contains(.,'My first course')]").is_displayed()
            assert False
        except NoSuchElementException:
            assert True


    def test_view_course_with_login(self, set_up):
        driver = set_up
        driver.get(MOODLE_URL)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        # Log in a student
        driver.find_element(By.ID, "username").send_keys(STUDENT_USERNAME)
        driver.find_element(By.ID, "password").send_keys(STUDENT_PASSWORD)
        driver.find_element(By.ID, "loginbtn").click()

        # Check if the student can view the course
        driver.get("{}course/view.php?id=2".format(MOODLE_URL))
        assert driver.find_element(By.XPATH, "//h1[contains(.,'My first course')]").is_displayed() == True
        try:
            driver.find_element(By.CSS_SELECTOR, "form[id='login']").is_displayed()
            assert False
        except NoSuchElementException:
            assert True
