from selenium import webdriver
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--lang', default='en')
parser.add_argument('--suite', default='home_page_tests/test_suite.py')
args, _ = parser.parse_known_args()

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://www.goal.com/{0}'.format(args.language))
print(args.suite)
print(browser.title)
assert bool(browser.title) == True
