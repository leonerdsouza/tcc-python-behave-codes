from selenium.webdriver.common.by import By 

class Locator:
    def __init__(self,l_type,selector):
        self.l_type = l_type
        self.selector = selector
    
    def parameterize(self,*args):
        self.selector = self.selector.format(*args)

class TestPageLocators:
    google_logo = Locator(By.XPATH, '/html/body/div[1]/div[2]/div/img')
    alert_login = Locator(By.XPATH, '/html/body/div[1]')
    product_page = Locator(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/span')
    item = Locator(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/span')
    text = Locator(By.XPATH,'/html/body/div[1]/div/div/div[2]/div')