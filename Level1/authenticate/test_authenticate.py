import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import json

MOODLE_URL = "https://sandbox400.moodledemo.net/"
MAX_TIMEOUT = 3
INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.json")

@pytest.fixture(scope="class")
def set_up():
    # Initialize a webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(MAX_TIMEOUT)

    yield driver  # This will return the driver to the test
    # Teardown actions go here
    driver.quit()

def get_input_data():
    with open(INPUT_PATH, "r", encoding='UTF-8') as f:
        data = json.load(f)
    return [(d["id"], d["username"], d["password"], d["expected"]) for d in data]

@pytest.mark.usefixtures("set_up")
class TestAuthenticate:
    

    @pytest.mark.parametrize("id,username,password,expected", get_input_data())
    def test_authenticate(self, set_up, id, username, password, expected):
        driver = set_up

        if username != "" and password != "":
            driver.get(MOODLE_URL)
            driver.find_element(By.LINK_TEXT, "Log in").click()
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "loginbtn").click()

        driver.get("{}course/view.php?id=2".format(MOODLE_URL))

        if expected == "display_course":
            assert driver.find_element(By.XPATH, "//h1[contains(.,'My first course')]").is_displayed() == True
            try:
                driver.find_element(By.CSS_SELECTOR, "form[id='login']").is_displayed()
                assert False
            except NoSuchElementException:
                assert True
        elif expected == "display_login_form":
            assert driver.find_element(By.CSS_SELECTOR, "form[id='login']").is_displayed() == True
            try:
                driver.find_element(By.XPATH, "//h1[contains(.,'My first course')]").is_displayed()
                assert False
            except NoSuchElementException:
                assert True
