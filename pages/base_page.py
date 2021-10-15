#from selenium import webdriver
#browser = webdriver.chrome('C:\\Users\\vavil\\Desktop\\chromedriver.exe')

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
