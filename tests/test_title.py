from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--lang', default='en')
parser.add_argument('--suite', default='home_page_tests/test_suite.py')
args, _ = parser.parse_known_args()

options = Options()  
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.goal.com/{0}'.format(args.lang))
print(args.suite)
print(browser.title)
assert bool(browser.title) == True
