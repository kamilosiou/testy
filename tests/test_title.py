from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--lang', default='en')
parser.add_argument('--suite', default='home_page_tests/test_suite.py')
args, _ = parser.parse_known_args()

chrome_options = Options()  
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
browser.get('https://www.goal.com/{0}'.format(args.language))
print(args.suite)
print(browser.title)
assert bool(browser.title) == True
