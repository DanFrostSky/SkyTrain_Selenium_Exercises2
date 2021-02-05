import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = object

def find(driver):
    qa = driver.find_element_by_id("qa")
    if qa:
        return qa
    else:
        return False

def setup_module():
    global driver
    global driver2

    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')
    #driver2 = webdriver.Chrome('https://google.com')

def teardown_module():
    driver.close()
    driver.quit()


def test_current_location():

    driver.get('c:\\work\\selenium-basics\\practice_page.html')

    result = driver.current_url
    print(result)
    expectedResult = "file:///C:/work/selenium-basics/practice_page.html"

    assert result == expectedResult


def test_navigate_to_between_sites():

    driver.get('c:\\work\\selenium-basics\\practice_page.html')

    #arrange
    bbc = driver.find_element_by_id("bbc")   
    qa = driver.find_element_by_id("qa")
    expectedResult_bbc = bbc.get_attribute('href')
    expectedResult_qa = qa.get_attribute('href')
    
    #act
    bbc.click()

    current_page = driver.current_url
    #assert
    assert expectedResult_bbc == current_page

    #act part 2
    driver.back()
    qa = WebDriverWait(driver, 2).until(find)
    qa.click()

    current_page = driver.current_url #are rewriting the variable current_page
    print(current_page)             #to the new webpage, don't need to define
    #assert part 2                     #new variable
    assert expectedResult_qa == current_page

#driver2.get

#driver.window_handles

#driver.switch_to.window(driver.window_handles[1])
