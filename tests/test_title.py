from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.google.pl/')
print(browser.title)
