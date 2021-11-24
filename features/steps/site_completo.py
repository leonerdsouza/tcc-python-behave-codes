from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC 
from pages.locators import TestPageLocators
import time

@given('I am at home page')
def step_impl(context):
    if context.browser.current_url != 'https://www.saucedemo.com/':
        message = 'current url is not expected url'
        raise Exception(message)

@when('I login into the site')
def step_impl(context):
    context.browser.find_element_by_id('user-name').send_keys('standard_user')
    context.browser.find_element_by_id('password').send_keys('secret_sauce')
    context.browser.find_element_by_id('login-button').click()

@then('I am logged at Products page')
def step_impl(context):
    WebDriverWait(context.browser,10).until(EC.text_to_be_present_in_element((TestPageLocators.product_page.l_type, TestPageLocators.product_page.selector),'PRODUCTS'))

@then('I click on Sauce Labs Backpack')
def step_impl(context):
    context.browser.find_element_by_link_text('Sauce Labs Backpack').click()


@then('I add the item to the shopping cart')
def step_impl(context):
    context.browser.find_element_by_id('add-to-cart-sauce-labs-backpack').click()

@then('I click on the cart button')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
    

@then('I proceed to checkout the product')
def step_impl(context):
    context.browser.find_element_by_id('checkout').click()


@then('I fill in the Personal Information')
def step_impl(context):
    context.browser.find_element_by_id('first-name').send_keys('Leonardo')
    context.browser.find_element_by_id('last-name').send_keys('Souza')
    context.browser.find_element_by_id('postal-code').send_keys('333333')
    context.browser.find_element_by_id('continue').click()
    

@then('I should see the overview page')
def step_impl(context):
    WebDriverWait(context.browser,10).until(EC.text_to_be_present_in_element((TestPageLocators.item.l_type, TestPageLocators.item.selector),'CHECKOUT: OVERVIEW'))


@then('I click on the finish button')
def step_impl(context):
    context.browser.find_element_by_id('finish').click()

@then('I  should see the order has been completed')
def step_impl(context):
    WebDriverWait(context.browser,10).until(EC.text_to_be_present_in_element((TestPageLocators.text.l_type, TestPageLocators.text.selector),'Your order has been dispatched, and will arrive just as fast as the pony can get there!'))