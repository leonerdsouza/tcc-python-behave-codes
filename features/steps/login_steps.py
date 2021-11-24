from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC 
from pages.locators import TestPageLocators


@given('I am at login page')
def step_impl(context):
    if context.browser.current_url != 'https://seubarriga.wcaquino.me/login':
        message = 'current url is not expected url'
        raise Exception(message)


@when('I try to login')
def step_impl(context):
    context.browser.find_element_by_id('email').send_keys('leo2@leo.com')
    context.browser.find_element_by_id('senha').send_keys('aaaa')
    context.browser.find_element_by_xpath('/html/body/div[2]/form/button').click()

@then('I am logged in')
def step_impl(context):
    WebDriverWait(context.browser,10).until(EC.presence_of_element_located((TestPageLocators.alert_login.l_type, TestPageLocators.alert_login.selector)))
    WebDriverWait(context.browser,10).until(EC.text_to_be_present_in_element((TestPageLocators.alert_login.l_type, TestPageLocators.alert_login.selector),'Bem vindo, leonardo!'))


    