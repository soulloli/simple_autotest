from functions import *
import time
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.uat
@pytest.mark.stage
def test_pp_2(driver):
    id = read(A)
    driver.get(f'{PpUrl}request/{id}/step/2')
    time.sleep(2)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(pp_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(pp_password)
    login_button = driver.find_element_by_xpath(simple_tag)
    login_button.click()
    time.sleep(20)
    form_passport = driver.find_elements_by_xpath(A)
    form_passport [0].send_keys("../Pictures/36624fdd-575b-4467-a15b-2b1d5d79a7ff.pdf")
    time.sleep(5)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(20)
    form_passport [1].send_keys(file())
    time.sleep(30)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(5)


@pytest.mark.uat
@pytest.mark.stage
def test_tag(driver):
    id = read(A)
    driver.get(
        f'{VerUrl}?referer=&query={id}')
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(ver_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(ver_password)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(7)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(1)
    driver.find_element_by_xpath(simple_tag).send_keys(UserVer + Keys.RETURN)
    time.sleep(10)
    driver.switch_to.window(driver.window_handles [-1])
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_id(simple_tag).send_keys(simple_date)
    time.sleep(2)
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_id(A)
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    driver.find_element_by_id(simple_tag).click()
    driver.find_element_by_css_selector(simple_tag).click()
    time.sleep(1.5)
    driver.close()


@pytest.mark.uat
@pytest.mark.stage
def test_ver_children(driver):
    i = 0
    driver.get(VerUrl)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(ver_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(ver_password)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(7)
    id = read(A)
    while i < 2:
        driver.get(
            f'{VerUrl}?referer=&query={id}')
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(1)
        driver.find_element_by_xpath(simple_tag).send_keys(UserVer + Keys.RETURN)
        time.sleep(10)
        driver.switch_to.window(driver.window_handles [-1])
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        i += 1


@pytest.mark.uat
@pytest.mark.stage
def test_ver_spouse(driver):
    i = 0
    driver.get(VerUrl)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(ver_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(ver_password)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(7)
    id = read(A)
    while i < 2:
        driver.get(
            f'{VerUrl}?referer=&query={id}')
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(1)
        driver.find_element_by_xpath(simple_tag).send_keys(UserVer + Keys.RETURN)
        time.sleep(10)
        driver.switch_to.window(driver.window_handles [-1])
        time.sleep(5)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        driver.find_element_by_css_selector(simple_tag).click()
        time.sleep(2)
        driver.find_element_by_css_selector(simple_tag).click()
        i += 1
        time.sleep(1.5)
