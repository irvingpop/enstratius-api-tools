#!/usr/bin/env python

# This script will now return the name of the group being created, and the ID

from mixcoatl.admin.group import Group
from mixcoatl.admin.user import User
from prettytable import PrettyTable
import argparse
import pprint
import esid
import resource_filter
import sys

def print_verbose(name,gid):
    print name, gid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', help='The name of the group.')
    parser.add_argument('--description', '-d', help='The description of the group.')
    parser.add_argument('--verbose', '-v', action='store_true', default=False, help='Print out verbose information about the group creation.')

    cmd_args = parser.parse_args()

    if cmd_args.name is None or cmd_args.description is None:
        parser.print_help()
        sys.exit(1)

    new_group = Group()

    new_group.description = cmd_args.description
    new_group.name = cmd_args.name

    result = new_group.create()

    if cmd_args.verbose:
        print_verbose(cmd_args.name, result['groups'][0]['groupId'])
    else:
        print result['groups'][0]['groupId']