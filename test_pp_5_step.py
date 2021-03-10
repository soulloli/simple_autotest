from functions import *
import time
import pytest


@pytest.mark.uat
@pytest.mark.stage
def test_pp_5(driver):
    id = read(A)
    driver.get(f'{PpUrl}request/{id}/step/5')
    time.sleep(2)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(pp_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(pp_password)
    login_button = driver.find_element_by_xpath(simple_tag)
    login_button.click()
    time.sleep(10)
    try:
        driver.find_element_by_css_selector(simple_tag).click()
        time.sleep(10)
        driver.find_element_by_xpath(simple_tag).click()
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(10)
        driver.find_element_by_xpath(simple_tag).click()
        driver.find_element_by_xpath(simple_tag).click()
        driver.find_element_by_xpath(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        time.sleep(10)
        driver.find_element_by_css_selector(simple_tag).click()
    except:
        pass
    time.sleep(20)
    driver.find_element_by_css_selector(simple_tag).click()
    time.sleep(10)
