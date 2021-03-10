import time
import pytest

from selenium.webdriver.common.keys import Keys

from functions import *

last_name = random_string()
first_name = random_string()


@pytest.mark.uat
@pytest.mark.stage
def test_pp_1(driver):
    driver.get(PpUrl)
    time.sleep(2)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(pp_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(pp_password)
    login_button = driver.find_element_by_xpath(simple_tag)
    login_button.click()
    time.sleep(10)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(10)
    # заполнение формы
    form_fname = driver.find_element_by_xpath(simple_tag)
    form_fname.send_keys(simple_date)
    form_sname = driver.find_element_by_xpath(simple_tag)
    form_sname.send_keys(simple_date)
    form_phone = driver.find_element_by_xpath(simple_tag)
    form_phone.send_keys(random_phone())
    form_experience = driver.find_element_by_xpath(simple_tag)
    form_experience.click()
    time.sleep(1)
    driver.find_element_by_xpath(simple_tag).click()
    form_passport = driver.find_elements_by_xpath(A)
    form_passport[0].send_keys("../Pictures/1.png")
    form_passport[1].send_keys("../Pictures/1.png")
    time.sleep(5)
    next_button = driver.find_element_by_xpath(simple_tag)
    next_button.click()
    url = driver.current_url
    len_url = len(f'{PpUrl}request/')
    write_url(url[len_url:-7])
    time.sleep(10)


@pytest.mark.uat
@pytest.mark.stage
def test_ver_fio(driver):
    i = 0

    driver.get(VerUrl)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(ver_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(ver_password)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(7)
    passport()
    id = read("url.txt")
    while i < 2:
        driver.get(f"{VerUrl}?referer=&query={id}")
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(1)
        driver.find_element_by_xpath(simple_tag).send_keys(UserVer + Keys.RETURN)
        time.sleep(10)
        driver.switch_to.window(driver.window_handles [-1])
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        try:
            driver.find_element_by_id(simple_tag).click()
            driver.find_element_by_id(simple_tag).send_keys(read(A))
        except:
            pass
        try:
            driver.find_element_by_id(simple_tag).send_keys(simple_date)
        except:
            pass
        try:
            driver.find_element_by_id(simple_tag).send_keys(simple_date)
        except:
            pass
        try:
            driver.find_element_by_css_selector(simple_tag).click()
            driver.find_element_by_css_selector(simple_tag).click()
        except:
            pass
        try:
            driver.find_element_by_id(simple_tag).click()
            driver.find_element_by_id(simple_tag).send_keys(simple_date)
        except:
            pass
        try:
            driver.find_element_by_id(simple_tag).click()
            driver.find_element_by_id(simple_tag).send_keys(simple_date)
        except:
            pass
        try:
            driver.find_element_by_css_selector(simple_tag).click()
        except:
            pass
        time.sleep(3)
        driver.find_element_by_css_selector(simple_tag).click()
        time.sleep(10)
        i += 1


@pytest.mark.stage
def test_ver_adress(driver):
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
            f"{VerUrl}?referer=&query={id}")
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(1)
        driver.find_element_by_xpath(simple_tag).send_keys(UserVer + Keys.RETURN)
        time.sleep(10)
        driver.switch_to.window(driver.window_handles [-1])
        time.sleep(5)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()

        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simple_date)
        time.sleep(5)
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(3)
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(10)
        i += 1


@pytest.mark.stage
def test_ver_issueBy(driver):
    i = 0
    driver.get(VerUrl)
    login = driver.find_element_by_xpath(simple_tag)
    login.send_keys(ver_login)
    password = driver.find_element_by_xpath(simple_tag)
    password.send_keys(ver_password)
    driver.find_element_by_xpath(simple_tag).click()
    time.sleep(7)
    id = read("url.txt")
    while i < 2:
        driver.get(
            f"{VerUrl}?referer=&query={id}")
        driver.find_element_by_xpath(simple_tag).click()
        time.sleep(1)
        driver.find_element_by_xpath(simple_tag).send_keys(UserVer + Keys.RETURN)
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simpe_date)
        # time.sleep(1.5)
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simpe_date)
        driver.find_element_by_id(simple_tag).click()
        driver.find_element_by_id(simple_tag).send_keys(simpe_date)
        driver.find_element_by_css_selector(simple_tag).click()
        driver.find_element_by_css_selector(simple_tag).click()
        i += 1
        time.sleep(2)
