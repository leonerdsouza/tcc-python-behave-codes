from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC 
from pages.locators import TestPageLocators
import time



@given('I am at main page')
def step_impl(context):
    if context.browser.current_url != 'https://www.google.com/':
        message = 'current url is not expected url'
        raise Exception(message)
        

@when('I try to find element Google Logo')
def step_impl(context):
    WebDriverWait(context.browser,10).until(EC.presence_of_element_located((TestPageLocators.google_logo.l_type, TestPageLocators.google_logo.selector)))

