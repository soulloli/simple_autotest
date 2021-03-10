from functions import *
import time
import pytest


@pytest.mark.uat
@pytest.mark.stage
def test_pp_4(driver):
    id = read(A)
    driver.get(f'{PpUrl}request/{id}/step/4')
    time.sleep(2)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(pp_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(pp_password)
    login_button = driver.find_element_by_xpath(simple_tag)
    login_button.click()
    time.sleep(10)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(5)
    driver.find_element_by_xpath(simple_tag).click()
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(4)
    driver.find_element_by_xpath(simple_tag).click()
    driver.find_element_by_xpath(simple_tag).send_keys(0)

    driver.find_element_by_xpath(simple_tag).click()
    driver.find_element_by_xpath(simple_tag).send_keys(
        random_string()
    )
    driver.find_element_by_xpath(simple_tag).send_keys(
        random_string()
    )
    driver.find_element_by_xpath(simple_tag).send_keys(
        random_string()
    )
    driver.find_element_by_xpath(simple_tag).send_keys(simple_date)
    driver.find_element_by_xpath(simple_tag).send_keys(
        random_phone()
    )
    driver.find_element_by_xpath(simple_tag).send_keys(simple_date)
    driver.find_element_by_xpath(simple_tag).send_keys(simple_date)
    form_passport = driver.find_elements_by_xpath(A)
    form_passport [0].send_keys("../Pictures/2.jpg")
    time.sleep(3)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(5)
