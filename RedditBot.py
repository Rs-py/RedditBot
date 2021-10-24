from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
import schedule 

#v2 Final - Push = Blocked
#UPDATE TO USE ALL CSS AS IT IS MORE RELIABLE SINCE IT USES ELEMENTS INSTEAD OF NAVIGATION
#ALSO XPATH IS DOIFFERENT FOR EACH BROWSER CAUSING PROBLEMS; CSS IS ALSO FASTER 

forumlist = [#Enter List of forums here]  





options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(firefox_options=options)

time.sleep(3) 

driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

entername = driver.find_element_by_id("loginUsername")
entername.send_keys("#EnterUsername")

time.sleep(2)

enterpw = driver.find_element_by_id("loginPassword")
enterpw.send_keys("#EnterPassword")

time.sleep(1) 

p_loginl = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click() 

time.sleep(20) 


def postjob():
    for x in forumlist:

        gopost = driver.find_element_by_css_selector("button._1x6pySZ2CoUnAfsFhGe7J1").click() 
        #gopost = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div[2]/div/div[1]/span[3]/button").click()

        time.sleep(10) 
        enterforum = driver.find_element_by_css_selector("._1MHSX9NVr4C2QxH2dMcg4M")
        #enterforum = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/input")
        enterforum.clear() 
        enterforum.send_keys(x)

        time.sleep(3)



        jstitletext = """
          var elm = arguments[0], txt = arguments[1];
          elm.value += txt;
          elm.dispatchEvent(new Event('change'));
          """

        entertitletext = driver.find_element_by_css_selector("._2wyvfFW3oNcCs5GVkmcJ8z > textarea:nth-child(1)")
        titletext = "#EnterTitleTextHere"

        driver.execute_script(jstitletext, entertitletext, titletext)
        entertitletext.clear() #Title was being entered twice so this clears first entry
        entertitletext.send_keys(titletext)

        time.sleep(1)


        jsmaintext = """
          var elm = arguments[0], txt = arguments[1];
          elm.value += txt;
          elm.dispatchEvent(new Event('change'));
          """
        entermaintext = driver.find_element_by_css_selector("#SHORTCUT_FOCUSABLE_DIV > div:nth-child(4) > div > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._1vyLCp-v-tE5QvZovwrASa > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2udhMC-jldHp_EpAuBeSR1.PaJBYLqPf_Gie2aZntVQ7 > div.HOFZo2X7Fr6JVBztpsByj > div._3w_665DK_NH7yIsRMuZkqB > div._1zq6UabIEJJ-z9grsiCJY7 > div:nth-child(2) > div > div > div._2baJGEALPiEMZpWB2iWQs7 > div > div:nth-child(1) > div > div > div")
        #entermaintext = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/span/span")
        maintext = "#EnterMainTextHere"

        driver.execute_script(jstitletext, entermaintext, maintext)
        entermaintext.send_keys(maintext)

        time.sleep(2)

        time.sleep(1)
        p_submit = driver.find_element_by_css_selector("._18Bo5Wuo3tMV-RDB8-kh8Z").click()
        #p_submit = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button").click()
        
        now = datetime.now().time()
        time.sleep(10)
        
        urlrn = driver.current_url

        if urlrn != "https://www.reddit.com/submit":
            print("Successfully posted to ", x ,"at", now,".")
        
        time.sleep(40)



schedule.every(30).minutes.do(postjob)

while True:
    schedule.run_pending()
    time.sleep(1)

