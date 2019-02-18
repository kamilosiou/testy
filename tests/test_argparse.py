import argparse

parser = argparse.ArgumentParser()
parser.add_argument("language")
args = parser.parse_args()

print args.language
