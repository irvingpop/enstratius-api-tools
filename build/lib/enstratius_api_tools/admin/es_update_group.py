#!/usr/bin/env python

from mixcoatl.admin.group import Group
from mixcoatl.admin.user import User
from prettytable import PrettyTable
import argparse
import pprint
import esid
import resource_filter
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--group_id', '-g', type=int, help='Group ID')
    parser.add_argument('--name', '-n', help='The name of the group.')
    parser.add_argument('--description', '-d', help='The description of the group.')

    cmd_args = parser.parse_args()

    if (cmd_args.group_id is None or (cmd_args.group_id is not None and (cmd_args.description is None and cmd_args.name is None))):
        parser.print_help()
        sys.exit(1)

    gid=cmd_args.group_id
    group_name=cmd_args.name
    group_description=cmd_args.description

    group = Group(gid)

    if (group_description is None and group_name is not None):
        result = group.updateName(group_name)
    elif (group_name is None and group_description is not None):
        result = group.updateDescription(group_description)
    else:
        result = group.update(group_name,group_description)
