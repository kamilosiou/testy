import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--language")
parser.add_argument("--pf_domain")
parser.add_argument("--browser")
parser.add_argument("--secure")

args = parser.parse_args()

print args
