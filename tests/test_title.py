from selenium import webdriver
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--language', default='en')
args, _ = parser.parse_known_args()

browser = webdriver.Chrome()
browser.get('https://www.goal.com/{0}'.format(args.language))
print(browser.title)
assert bool(browser.title) == True
