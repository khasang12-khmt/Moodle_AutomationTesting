from selenium import webdriver
from selenium.webdriver.common.by import By
from constant import SANDBOX_URL
import time
import logging
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.WARNING)
current_directory = os.path.dirname(__file__)
JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

def drop_files(element, files, offsetX=0, offsetY=0):
    driver = element.parent
    isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    paths = []
    
    # ensure files are present, and upload to the remote server if session is remote
    for file in (files if isinstance(files, list) else [files]) :
        if not os.path.isfile(file) :
            raise FileNotFoundError(file)
        paths.append(file if isLocal else element._upload(file))
    
    value = '\n'.join(paths)
    elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})
    
    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fp-file")))

WebElement.drop_files = drop_files

class PerformanceTask:
    def __init__(self,**kwargs):
        self.driver = None

    def _setup_method(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)

    def _teardown_method(self):
        if self.driver:
            self.driver.quit()

    def _precondition(self):
        pass

    def _logout(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

    def run_task(self):
        try:
            self._setup_method()
            result = self._task()
            self._teardown_method()
            return result
        except Exception as err:
            raise Exception(f"Unexpected {err=}, {type(err)=}")

class LoginTask(PerformanceTask):
    def __init__(self,**kwargs):
        super().__init__()
        
    def precondtion(self):
      self.driver.get(SANDBOX_URL)
      self.driver.set_window_size(787, 816)
      self.driver.find_element(By.LINK_TEXT, "Log i").click()
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").clear()
      self.driver.find_element(By.ID, "username").send_keys("teacher")
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "password").send_keys("sandbox")
      self.driver.find_element(By.ID, "loginbtn").click()
      
    def _task(self):
        try:
            self.precondtion()
            self._logout()
            return True
        except Exception as err:
            return Exception(f"Unexpected {err=}, {type(err)=}")
        
class GoToCourseTask(PerformanceTask):
    def __init__(self, **kwargs):
        super().__init__()
        
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
      
    def _task(self):
        try:
            self.precondtion()
            wait = WebDriverWait(self.driver, 10)
            course = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-region='course-content']")))
            course.click()
            time.sleep(1)
            self._logout()
            return True
        except Exception as err:
            return Exception(f"Unexpected {err=}, {type(err)=}")
        
class UploadImageTask(PerformanceTask):
    def __init__(self, **kwargs):
        super().__init__()
        self.image_path = kwargs['image_path']
        
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
      self.driver.find_element(By.ID, "user-menu-toggle").click()
      self.driver.find_element(By.LINK_TEXT, "Profile").click()
      self.driver.find_element(By.LINK_TEXT, "Edit profile").click()
      
    def _task(self):
        try:
            self.precondtion()
            wait = WebDriverWait(self.driver, 20)
            file_path = os.path.abspath(self.image_path)
            wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.filemanager-container')))
            drop_target = self.driver.find_element(By.CSS_SELECTOR, '.filemanager-container')
            drop_target.drop_files(file_path) 
            self._logout()
            return True
        except Exception as err:
            return Exception(f"Unexpected {err=}, {type(err)=}")
        
