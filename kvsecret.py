#!/usr/bin/env python

import argparse

""" Class for defining and enabling KVsecret CLI. """
class kvsecret:

    """ Initialize the kvsecret class. """
    def __init__(self):
        self.version = '0.0.1'

    def logo():
        print('Some day there will be ASCIart here\n')

    def cli():
        parser = argparse.ArgumentParser(prog='kvsecret', description='A command-line tool for managing secrets.', epilog='Developed by Wesley Weidenhamer.')

        parser.add_argument('-v', action='version', version='%(prog)s v' + self.version, help='display %(prog)s version.')
        if len(sys.argv) < 2:
            logo()
            parser.print_help()
            sys.exit(1)
        
        return parser.parse_args()

    def main():
        args = cli()

kvsecret()
