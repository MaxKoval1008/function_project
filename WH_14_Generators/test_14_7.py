import sys
import argparse

print(sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('echo')
args = parser.parse_args()
print(args)
print('First name: ', args.first_name)
print('Last name: ', args.last_name)
print('echo: ', args.echo)
print(sys.platform)
# для вызова файла в консоли вводится: python3 test_14_7.py -fn Max -ln Koval test
