from selenium import webdriver
import time

driver = webdriver.Firefox()

time.sleep(3)

driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

entername = driver.find_element_by_id("loginUsername")
entername.send_keys("#EnterLoginHere")

time.sleep(2)

enterpw = driver.find_element_by_id("loginPassword")
enterpw.send_keys("#EnterPasswordHere")

time.sleep(1)

p_loginl = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()

time.sleep(10)

def post():
  gopost = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div[2]/div/div[1]/span[3]/button").click()

  time.sleep(3)

  enterforum = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/input")
  enterforum.send_keys("#EnterForumNameHere")

  time.sleep(3)

  entertitle = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea")
  entertitle.send_keys("#EnterTitleHere")

  time.sleep(1)

  #entermaintext = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div")

  jstext = """
    var elm = arguments[0], txt = arguments[1];
    elm.value += txt;
    elm.dispatchEvent(new Event('change'));
    """

  entermaintext = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div")
  maintext = "#EnterMainText"


  driver.execute_script(jstext, entermaintext, maintext)
  entermaintext.send_keys(maintext)

  time.sleep(2)



  time.sleep(1)
  p_submit = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button").click()
