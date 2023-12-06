import time
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from constant import SANDBOX_URL

class TestMessage:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
    
    def precondtion(self):
        self.driver.get(SANDBOX_URL)
        self.driver.set_window_size(787, 816)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("sandbox")
        self.driver.find_element(By.ID, "loginbtn").click()
      
    def logout(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        
    def run(self, filename):
        with open(filename, "r") as file:
            testset = json.load(file)
        total = len(testset)
        success = 0
        fail = []
        for testcase in testset :
            id = testcase['id']
            print(f"Run testcase: {id}")
            self.setup_method(None)
            method_name = testcase["function"]
            method = getattr(self, method_name)
            try:
                result, valid = method(testcase["input"], testcase["expected"])
                if(result and valid):
                    success = success + 1
                else:
                    fail.append(id)
            except Exception as err:
                fail.append(f'{id} Error: {err=}')
            self.teardown_method(None)
    
        print(f"SUCESS: {success}/{total}")
        print(f"FAIL: {str(fail)}")
        return testset

    def test_message_length(self, data, expected):
        self.precondtion()
        result = None
        if data["type"] == "text":
            self.sendMessageFlow(data["value"])
            if data["value"] == "":  
                result = False
            elif self.check_message_send(data["value"]):
                result = True
            else: result = False
        else:
            self.sendIconFlow(data["n"], data["title"])
            result = True
        self.logout()
        return result, result == expected

    def test_message_usecase(self, data, expected):
        wait = WebDriverWait(self.driver, 10)
        self.precondtion()
        for step in data["steps"]:
            if step == "clickMessageShow":
                time.sleep(1)
                self.clickMessageShow()
            elif step == "clickConversationShow":
                time.sleep(1)
                self.clickConversationShow()
            elif step == "searchConversation":
                time.sleep(1)
                self.searchConversation(data["search_value"])
            elif step == "clickSearchResult":
                time.sleep(1)
                self.clickSearchResult()
            elif step == "sendMessage":
                time.sleep(1)
                self.sendMessage(data["message"])
            elif step == "clickPrivateConversation":
                time.sleep(1)
                self.clickConversationShow("private")
                raise Exception("No conversation")
            elif step == "clickConversation":
                data_user_id = data.get("data_user_id")
                if(data_user_id):
                    self.clickConversation(data_user_id)
                else:
                    self.clickConversation()
                time.sleep(1)
        self.logout()
        if (data["search_value"] == "" and data["value"] == "") or app.checker.check_message_send(data["value"]):
            return True, True == expected
        else: return False, False == expected
        
    def clickMessageShow(self):
        mess_drawer = self.driver.find_element(By.CSS_SELECTOR, "a[id^='message-drawer-toggle']")
        mess_drawer.click()

    def clickConversationShow(self, typ = "star"):
      id = None
      if typ == "star":
          id = "view-overview-favourites-toggle"
      elif typ == "group":
          id = "view-overview-group-messages-toggle"
      elif typ == "private":
          id = "view-overview-messages-toggle"
      else:
          raise Exception("incorrect type of conversation")

      wait = WebDriverWait(self.driver, 10)
      try:
          wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "py-0 px-2 d-flex list-group-item list-group-item-action align-items-center")))
      except: pass
      conver_btn = self.driver.find_element(By.ID, id).find_element(By.TAG_NAME, "button")
      if conver_btn.get_attribute("aria-expanded") == "false":
          conver_btn.click()
          
    def check_message_send(self, value):
        try:
            wait = WebDriverWait(self.driver, 10)
            divtag = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-region='message']")))[-1]
            lastmessage = divtag.find_element(By.TAG_NAME, "p").text
            return lastmessage == value
        except: return False

    def clickConversation(self, data_user_id = 3):
        wait = WebDriverWait(self.driver, 10)
        conv_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-user-id='{}']".format(data_user_id))))
        conv_btn.click()

    def clickSearchResult(self, user_id = 4):
        wait = WebDriverWait(self.driver, 10)
        convbtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[data-route='view-conversation'][data-route-param-1='false'][data-route-param-2='create'][data-route-param-3='4'][role='button']")))
        convbtn.click()

    def searchConversation(self, value):
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-region='view-overview-search-input']")))
        search_input.send_keys(value + "\n")

    def sendMessageFlow(self, mess, data_user_id = 3, network_condition=None):
        self.clickMessageShow()
        wait = WebDriverWait(self.driver, 10)
        self.clickConversationShow()
        self.clickConversation(data_user_id)
        textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-region='send-message-txt']")))
        if network_condition:
            if network_condition == "slow":
                self.driver.set_network_conditions(
                    offline=False,
                    latency=2000,  # In milliseconds
                    download_throughput=1 * 1024,  # In bytes/second
                    upload_throughput=1 * 1024  # In bytes/second
                )
            elif network_condition == "offline":
                self.driver.set_network_conditions(
                    offline=True,
                    latency=200,  # In milliseconds
                    download_throughput=100 * 1024,  # In bytes/second
                    upload_throughput=100 * 1024  # In bytes/second
                )
        textarea.send_keys(mess)
        send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='send-message']")))
        send_btn.click()
        time.sleep(2)

    def sendMessage(self, mess):
        wait = WebDriverWait(self.driver, 10)
        textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-region='send-message-txt']")))
        textarea.send_keys(mess)
        send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='send-message']")))
        send_btn.click()
        time.sleep(2)

    def sendIconFlow(self, n = 1, title = ":smile:", data_user_id = 3):
        self.clickMessageShow()
        wait = WebDriverWait(self.driver, 10)
        self.clickConversationShow()
        self.clickConversation(data_user_id)

        for i in range(n):
            iconbtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='toggle-emoji-picker']")))
            iconbtn.click()
            icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='{}']".format(title))))
            icon.click()
        
        send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='send-message']")))
        send_btn.click()
        time.sleep(2)

    def sendIcon(self, n = 1, title = ":smile:"):
        wait = WebDriverWait(self.driver, 10)

        for i in range(n):
            iconbtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='toggle-emoji-picker']")))
            iconbtn.click()
            icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='{}']".format(title))))
            icon.click()
        
        send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='send-message']")))
        send_btn.click()
        time.sleep(2)

TestMessage().run('./input/input_testMessage.json')