#!/usr/bin/env python

from mixcoatl.admin.user import User
from prettytable import PrettyTable
import argparse
import pprint
import sys

if __name__ == '__main__':
    """ Returns a list of users. """
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', help='Produce verbose output', action="store_true")

    cmd_args = parser.parse_args()

    users = User.all()
    if cmd_args.verbose:
        for user in users:
            user.pprint()
    else:
        user_table = PrettyTable(["User ID", "Last Name", "First Name", "Email", "Groups"])
        for user in users:
            group_list = []
            if hasattr(user, 'groups'):
                for group in user.groups:
                    group_list.append(group['name'])
            user_table.add_row([user.vm_login_id, user.family_name, user.given_name,
                                user.email, "\n".join(group_list)])
        print(user_table)