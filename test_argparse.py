import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--language")
parser.add_argument("--pf_domain")
parser.add_argument("--env")
args = parser.parse_args()

print args
