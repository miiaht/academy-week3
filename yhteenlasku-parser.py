#Argparser exercise for python

import argparse

parser = argparse.ArgumentParser(description='lasketaan yhteen!')
parser.add_argument("luku1", help="syota luku 1", type=int)
parser.add_argument("luku2", help="syota luku2", type=int)

args = parser.parse_args()
print(args.luku1 + args.luku2)