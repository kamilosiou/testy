import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--language")
parser.add_argument("--suite")

args = parser.parse_args()

print args.language
print args.suite
