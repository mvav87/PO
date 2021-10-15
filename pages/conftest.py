import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('C:\\Users\\vavil\\Desktop\\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()