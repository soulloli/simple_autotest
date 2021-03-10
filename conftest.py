import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="None", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = False
        driver = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
