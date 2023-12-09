import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

current_directory = os.path.dirname(__file__)
JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"


class TestMessage():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
    
  def precondtion(self):
      self.driver.get("https://sandbox.moodledemo.net/")
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
  
  def test_Message1(self):
      self.precondtion()
      try:
        self.sendMessageFlow("")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False

  def test_Message2(self):
      self.precondtion()
      try:
        self.sendMessageFlow("a")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False

  def test_Message3(self):
      self.precondtion()
      try:
        self.sendIconFlow(1)
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False    
      
  def test_Message4(self):
      self.precondtion()
      try:
        self.sendMessageFlow("c1]}XZnd-a3dTB4St&c:f4&xzG{;;{?j]P1tgyVgj7rbQh&hvC:)0WLQ@M*/*w;AwC9)@qztJUeT[xSXNp]k$:Kj)gcD,Q&k=u#+2yNJx@w8m2Nd2WfWSJwt0MGanKBTRz(-e5Y_]&rpG7:8C9LfqepN!NbtEDcSxq!@i!]NP+}7@B87Wm)T5tr4QHd@+(a[ATgZ3[wfJpyaAHhGZE1_7&)_EQ=!y}Bi}-2b/Kv#f-Z?,T90Y*+4akbvERCmS=,*tk&-TtvW+Pi6]3e+gDbD/R?Lc;!+?R]bKgnqaE-G#)#B!ZXa!G9Ck+6b8q_$N}p*K$9Cm7AG)Ry]=T5_5[[n_,dn-HZYp_aG7[nutDEz7&-L;%27/3r+FYLT$9)6nPbfB)cA-wW.zmHj2H9{PmHib7c[?Z[U/!fRUUGr**g!4}ZLn-TTF,+m&*k)=FCPUqMt51?q[}c%jz;T+;NLyDd0hn33erfv,YLLEPV&!b8MFScM0c}VJ+1vi5g-#;+wGc(zzU1E#-H+-DR$]p/?9SN+Lf8D*8UQ/R#t}5GvV9ew5zYhE8Q.npa22W_&SXimT[X6+wcL/93Ux6-=F,p6d6}W_+hC7RmtK(Z4?Ey$E_@x;$M4yH:W*N3uG$AqhJjn=i,Bz?6Axwf4*Ly]vk&zg+0G4_2r4-&@$/+N_eJK/BzV!r}_1DhLuaB3a1EX&}cXd{kc=vzjHGg5j{/i=fRbBYaZM0,ip2qmb?qe80Y}k,H1nM..xTYkL.(-y]U:r6t-+!m:Q4@8cV;z)fjgD8rV1V8VceM@%}yYz&wNt5@jU}Q$2?zM;CT!JC2(4KThW7EH,Cf=hSuq;4efu(N.-*U9wrak30V4xwt{{@6b%E{rxTt=CmqqkU,f:i99Hkp8{8TbG{nvy&HfeeX2Xw+PAbg!ch_3,rX38Pch7!MK#cxQM4QJK99R8Rq/2wa@QyxpX!*;W/myCx+,Wqc*(x#r_p4Xk$yzfuCF_G0x{V7#27xf,$7A8?E(]J#%3znFuf/:Lhwhv!dptj-7zSGB0}SvS_g!JL0,c!1p0%AN%7RNq)Z];5w5w7942&0Wq12T=KP09e(g{%d*wYzJ!d;Jgx1Ua_b*Qy6XSXXT1.:m_55HT#}Ub}bcTXNpt&n!Peb@C%/RC2rc*X%{[e/S}y.Q+z&-/#2(n$#b#wSgvQY3{fDe;EwW{.muf8/.Svpg%y4x{UC,FrG];i2hWXUr[vQz*Xk6Lfnm]He,Gf0F_3k[4qJ=p1(B=GN]F=1mQm.*i{,?&m8DH$,-NGSf{C?Qvcg-A,,bTHh9$8SmnLErv]$W#yR0q=}c_/rCWS;T0A5vG9ayu4#CF2cVD[/z3T./A&,/wprzRKEwZb/Q:Cy:26G,&j!_kpe;xP$7{4rvWAwTpAg!2N!Jbjghu[mM#{?pRG.NW]n0KY)qvyj%bNYgWwSfmJ+/eS+0u6YG0Ca[DbZeEq,ygp0Uv0+aYf#if?9JN3FmU#vn,Du7BgxuHNm/!N#r9d0ZU)X5c@m-w0)!CrG#irPUx7q5rYjr/8RMeTn%jAcaAR6gTU+m%P4}d=4U?XFD%ihQ;;?!(hrk0x=wyd23U,zf1}K#LEx9Z+hY]CeRGaB9f7XQ59wp1z!ap#_h));(+_Mg.PZBePq@,NCqkDLm[06;k=%H)]UYGE1;MLMF=4J200*:VJ=i4S%&(#/S:5n(ca5a5[$.&CjSee:c$FPmYw$Mp(3a%dh!SpDd5aR;$F8{GK$wQ$$H,YqgG[1mPekJd+SG(teK0+=EZ0{v,){ARX9m0;fHdCp{mR_1**4{eA{KgLf@x*0un)fT6N8Vxm,i@5/cDU-j}utpaV*E;+22$rE#ZD*v23&GB{1Cdj6@;H5QWj@)vW*E]F5*1_*}aR..YA0d);hLZk]B;){PiPSf.x(:5D7K$JF4!+6HWQ*L!8fi=tcGdyx2U6[eq/B%Awg{$g]naK$(vRAmHDNw,[8t;ZT/H7VSPRw)Xb;McZ)(=6Ht&4M1f8H$")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False

  def test_Message5(self):
      self.precondtion()
      try:
        self.sendIconFlow(100)
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False
      
  def test_Message6(self):
      self.precondtion()
      try:
        self.sendMessageFlow("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")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False
      
  def test_Message7(self):
      self.precondtion()
      try:
        self.sendMessageFlow("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")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False

  # def test_Message8(self):
  #     self.precondtion()
  #     try:
  #       self.sendIconFlow(2047)
  #       self.logout()
  #       return True
  #     except Exception as err:
  #       self.logout()
  #       return False
      
  # def test_Message9(self):
  #     self.precondtion()
  #     try:
  #       self.sendIconFlow(2048)
  #       self.logout()
  #       return True
  #     except Exception as err:
  #       self.logout()
  #       return False

  def test_Usecase_Message1(self):
      self.precondtion()
      try:
        self.sendMessageFlow("Hello World!")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False
  
  def test_Usecase_Message2(self):
      self.precondtion()
      try:
        self.clickMessageShow()
        self.searchConversation("Sam Student")
        self.clickSearchResult()
        self.sendMessage("Hello World!")
        time.sleep(2)
        self.logout()
        return True
      except Exception as err:
        print(err)
        self.logout()
        return False     

  def test_Usecase_Message3(self):
      self.precondtion()
      try:
        self.clickMessageShow()
        self.clickConversationShow(typ="private")
        self.logout()
        return True
      except Exception as err:
        self.logout()
        return False
  
  def test_Usecase_Message4(self):
      self.precondtion()
      try:
        self.clickMessageShow()
        self.searchConversation("abcdefasjdoaoljdfakisdkasndahsdjasdnakjsnd")
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[@data-region='no-results-container']")))
        self.logout()
        return True
      except Exception as err:
        print(err)
        self.logout()
        return False    
  
  def test_Usecase_Message5(self):
      self.precondtion()
      try:
        self.sendMessageFlow("Hello", network_condition="offline")
        time.sleep(2)
        sthWhenWrong = self.driver.find_element(By.XPATH, "//span[text()='Something went wrong!']")
        parent = sthWhenWrong.find_element(By.XPATH, "../../../..")
        retryBtn = parent.find_element(By.XPATH, ".//button[@data-region='retry-send']")
        retryBtn.click()
        time.sleep(1)
        self.driver.set_network_conditions(
            offline=False,
            latency=0,  # In milliseconds
            download_throughput=-1,  # In bytes/second
            upload_throughput=-1  # In bytes/second
        )
        retryBtn.click()
        time.sleep(1)
        self.logout()
        return True
      except Exception as err:
        print(err)
        self.logout()
        return False

  def test_Usecase_Message6(self):
      self.precondtion()
      try:
        self.sendMessageFlow("Hello", network_condition="offline")
        self.driver.find_element(By.XPATH, "//span[text()='Something went wrong!']")
        self.logout()
        return True
      except Exception as err:
        print(err)
        self.logout()
        return False

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
        convs[index].click()
    except TimeoutException as err:
        pass
      
  def clickSearchResult(self, index = 0):
    try:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-route='view-conversation']")))
        convs = self.driver.find_elements(By.CSS_SELECTOR, "a[data-route='view-conversation']")
        if len(convs) == 0:
            raise Exception("Empty Conversation List")
        convs[index].click()
    except TimeoutException as err:
        pass

  def searchConversation(self, value):
    wait = WebDriverWait(self.driver, 10)
    search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-region='view-overview-search-input']")))
    search_input.send_keys(value + "\n")

  def sendMessageFlow(self, mess, index = 0, network_condition=None):
      self.clickMessageShow()
      wait = WebDriverWait(self.driver, 10)
      self.clickConversationShow()
      self.clickConversation(index)
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

  def test(self, *test_list):
    result = []
    for test in test_list:
        result.append(test())
    fail_test_name = []
    for i in range(0, len(result)):
        if not result[i]:
            fail_test_name.append(test_list[i].__name__)

    fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
    return f"""    \n- Test Message (Level 0)--\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
    """

  def run(self):
    self.setup_method(None)
    test_methods = []
    test_methods = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith("test_Message")]
    test_methods = sorted(test_methods, key=lambda x: int(x.split('test_Message')[1]))
  
    test_Usecase_Message = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith("test_Usecase_Message")]
    test_Usecase_Message = sorted(test_Usecase_Message, key=lambda x: int(x.split('test_Usecase_Message')[1]))
    
    test_methods = test_methods + test_Usecase_Message

    result = self.test(*map(lambda mname: getattr(self, mname), test_methods))

    self.teardown_method(None)

    return result
  
testMessage = TestMessage()
print(testMessage.run())