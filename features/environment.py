import os
import datetime
from selenium import webdriver
from allure_behave.hooks import allure_report
from selenium.common.exceptions import WebDriverException
from context.config import settings

_file_path = os.path.dirname((__file__))
allure_report = (_file_path + "/results")

def browser_config(context, browser_name):
    if browser_name == "firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Firefox(firefox_options=option)
        return driver

    if browser_name == "headless-firefox":
        option = webdriver.FirefoxOptions()
        option.headless = True
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-gpu")
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--disable-application-cache")
        option.add_argument("--start-maximized")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Firefox(firefox_options=option)
        return driver

    if browser_name == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(chrome_options=option)
        return driver

    if browser_name == "headless-chrome":
        option = webdriver.ChromeOptions()
        option.headless = True
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-gpu")
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--disable-application-cache")
        option.add_argument("--start-maximized")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(chrome_options=option)
        return driver

def before_scenario(context, scenario):
    browser_name = settings.browser
    context.browser = browser_config(context, browser_name)
    context.browser.implicitly_wait(5)
    context.browser.set_page_load_timeout(60)
    context.location = settings.portal_url
    context.browser.get(context.location)

def after_scenario (context,scenario):
    try:
        if scenario.status == 'failed':
            context.browser.close()
        else:
            context.browser.close()
    except AttributeError or WebDriverException:
        message = "'Context' object has no attribute 'browser'\nChrome failed to start: exited abnormally"
        raise Exception(message)