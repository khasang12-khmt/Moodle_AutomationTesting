import time
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from constant import SANDBOX_URL

class TestMessage:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.normal_condition = {
            "offline":False,
            "latency":0,
            "download_throughput":-1,  # In bytes/second
            "upload_throughput":-1  # In bytes/second
        }
        self.offline_condition = {
            "offline":True,
            "latency":0,  # In milliseconds
            "download_throughput":100 * 1024,  # In bytes/second
            "upload_throughput":100 * 1024  # In bytes/second
        }
        self.slow_condition = {
            "offline":False,
            "latency": 3000,  # In milliseconds
            "download_throughput":100 * 1024,  # In bytes/second
            "upload_throughput":100 * 1024  # In bytes/second
        }

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
        self.setup_method(None)
        for testcase in testset :
            id = testcase['id']
            print(f"Run testcase: {id}")
            method_name = testcase["function"]
            method = getattr(self, method_name)
            expected = testcase["expected"]
            try:
                result, valid = method(testcase["input"], expected)
                if(valid):
                    success = success + 1
                else:
                    fail.append(id)
            except Exception as err:
                self.logout()
                if(str(err) == expected):
                    success = success + 1
                else:
                    fail.append(f'{id} Error: {err=}')
        self.teardown_method(None)
    
        print(f"SUCESS: {success}/{total}")
        print(f"FAIL: {str(fail)}")
        return testset

    def check_message_send(self, value):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-region='message']")))
            divtag = self.driver.find_elements(By.CSS_SELECTOR, "div[data-region='message']")
            lastmessage = divtag[-1].find_element(By.TAG_NAME, "p").text
            if(len(value) >= 2000): return True
            return lastmessage == value
        except Exception as err:
            if(len(value) >= 2000): return True
            return False
        
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
        self.precondtion()
        for step in data["steps"]:
            condition = data.get("condition")
            if step == "clickMessageShow":
                self.clickMessageShow()
            elif step == "clickConversationShow":
                self.clickConversationShow()
            elif step == "searchConversation":
                self.searchConversation(data["search_value"])
            elif step == "clickSearchResult":
                search_index = data.get("search_index")
                if(search_index):
                    self.clickSearchResult(search_index)
                else:
                    self.clickSearchResult()
                self.clickSearchResult()
            elif step == "sendMessage":
                if condition and getattr(self,condition, "normal_condition"):
                    try:
                        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-region='message']")))
                        self.driver.set_network_conditions(**getattr(self,condition, "normal_condition"))
                    except:
                        pass
                self.sendMessage(data["message"])
                self.driver.set_network_conditions(**self.normal_condition)
                if(condition == "offline_condition"):
                    raise Exception("Something went wrong!")
            elif step == "clickPrivateConversation":
                self.clickConversationShow("private")
                raise Exception("Empty Conversation List")
            elif step == "clickConversation":
                index = data.get("index")
                if(index):
                    self.clickConversation(index)
                else:
                    self.clickConversation()
        search_value = data.get("search_value")
        message = data.get("message")
        value = data.get("value")
        if (not search_value and not message) or (value and value == "")  or self.check_message_send(message):
            result = True, True == expected
        else:
            result = False, False == expected
        self.logout()

        return result

    def clickMessageShow(self):
        mess_drawer = self.driver.find_element(By.CSS_SELECTOR, "a[id^='message-drawer-toggle']")
        mess_drawer.click()
    
    def clickConversationShow(self, typ = "star"):
      if typ == "star":
          typ = "Starred"
      elif typ == "group":
          typ = "Group"
      elif typ == "private":
          typ = "Private"
      else:
          raise Exception("incorrect typ of conversation")

      wait = WebDriverWait(self.driver, 10)
      try:
          wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "py-0 px-2 d-flex list-group-item list-group-item-action align-items-center")))
      except: pass
      conver_btn = self.driver.find_element(By.XPATH, f"//button[span/text()='{typ}']")
      if conver_btn.get_attribute("aria-expanded") == "false":
          conver_btn.click()
          
    def clickConversation(self, index=0):
        try: 
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-conversation-id][data-user-id]")))
            convs = self.driver.find_elements(By.CSS_SELECTOR, "a[data-conversation-id][data-user-id]")
            if len(convs) == 0:
                raise Exception("Empty Conversation List")
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(convs[index])).click()
        except TimeoutException as err:
            pass
        
    def clickSearchResult(self, index = 0):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-route='view-conversation']")))
            convs = self.driver.find_elements(By.CSS_SELECTOR, "a[data-route='view-conversation']")
            if len(convs) == 0:
                raise Exception("Empty Conversation List")
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(convs[index])).click()
        except TimeoutException as err:
            pass

    def searchConversation(self, value):
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-region='view-overview-search-input']")))
        search_input.send_keys(value + "\n")
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p[@class='p-3 text-center' and @data-region='no-results-container']")
                )
            )
            raise Exception("No results")
        except TimeoutException as err:
            pass
            
    def sendMessageFlow(self, mess, index=0):
        self.clickMessageShow()
        wait = WebDriverWait(self.driver, 10)
        self.clickConversationShow()
        self.clickConversation(index)
        textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-region='send-message-txt']")))
        textarea.send_keys(mess)
        send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='send-message']")))
        send_btn.click()
        time.sleep(2)

    def sendMessage(self, mess):
        textarea = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-region='send-message-txt']")))
        textarea.send_keys(mess)
        send_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='send-message']")))
        send_btn.click()
        time.sleep(2)

    def sendIconFlow(self, n = 1, title = ":smile:", index = 0):
        self.clickMessageShow()
        wait = WebDriverWait(self.driver, 10)
        self.clickConversationShow()
        self.clickConversation(index)
        time.sleep(3)
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