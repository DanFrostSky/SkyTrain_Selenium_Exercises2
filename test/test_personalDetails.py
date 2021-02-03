import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains



def setup_module():
    global driver

    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')
   

def teardown_module():
    driver.close()
    driver.quit()


#def test_verify_username():

   # driver.get('c:\\work\\selenium-basics\\practice_page.html')

   # username = driver.find_element_by_id("username")
   # username.send_keys("species8472")

    #expectedResult = "species8472"
    #result = username.get_attribute("value")

   # driver.close()

    #assert expectedResult == result

def test_capitalise_firstname():

    driver.get('c:\\work\\selenium-basics\\practice_page.html')

    first_name = driver.find_element_by_id("firstname")
    first_name.send_keys("daniel")
    last_name = driver.find_element_by_id("lastname")

    last_name.click()

    expectedResult = "Daniel"
    result = first_name.get_attribute("value")

    assert expectedResult == result

def test_capitalise_lastname():

    driver.get('c:\\work\\selenium-basics\\practice_page.html')

    last_name = driver.find_element_by_id("lastname")
    last_name.send_keys("frost")
    first_name = driver.find_element_by_id("firstname")

    first_name.click()

    expectedResult = "Frost"
    result = last_name.get_attribute("value")

    assert expectedResult == result

def test_age_label_initially_blank():

    driver.get('c:\\work\\selenium-basics\\practice_page.html')

    age = driver.find_element_by_id('age')

    expectedResult = "XXX"
    result = age.get_attribute("innerText")

    assert expectedResult == result

def test_correct_age_displayed():

    driver.get('c:\\work\\selenium-basics\\practice_page.html')

    birthday = driver.find_element_by_id("birthday")
    birthday.send_keys("08-01-1993")

    age = driver.find_element_by_id('age')

    expectedResult = "28"
    result = age.get_attribute("innerText")
    
    assert expectedResult == result










