import argparse

languages = ['en',
             'en-gb',
             'de']


parser = argparse.ArgumentParser()
parser.add_argument("--suite")

args = parser.parse_args()

for language in languages:
  print language
  print args.suite
