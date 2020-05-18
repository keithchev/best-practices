import os
import sys
import json
import argparse


def parse_args():
    '''
    '''
    parser = argparse.ArgumentParser()

    # a positional argument
    parser.add_argument('positional_arg_1')

    # a second positional argument
    parser.add_argument('positional_arg_2')

    # an optional parameters
    parser.add_argument('--optional-param', dest='optional_param')

    args = parser.parse_args()
    return args


def main():
    '''
    '''
    args = parse_args()

    print('Positional argument 1 is %s' % args.positional_arg_1)
    print('Positional argument 2 is %s' % args.positional_arg_2)

    if args.optional_param is not None:
        print('Optional parameter: %s' % args.optional_param)


if __name__ == '__main__':
    main()
