#!/usr/bin/env python

# Updates an acl on a role

# This script can work to add ACL one at a time like this:
# es-set-acl.py -r 55600 -R VOLUME -a Attach -q MINE
#
# or it can read rules from an input file. If an input file is provided,
# -a, -q, and -R arguments are ignored, even if they are specified.
#
# The format of the input file should be json. Here is an example:
#
#
# {
#     "access": [
#         {
#             "action": "Configure",
#             "qualifier": "THIS_GROUP",
#             "resourceType": "IMAGE",
#             "role": 51200
#         },
#         {
#             "action": "UseAPI",
#             "qualifier": "ANY",
#             "resourceType": "CONSOLE",
#             "role": 51200
#         },
#         {
#             "action": "Attach",
#             "qualifier": "MINE",
#             "resourceType": "VOLUME",
#             "role": 51200
#         }
# 	]
# }

# The script will check to see if the file is in proper JSON format before trying
# to use it to add ACL rules to a role.
#
# To Do: Enumerate all of the resource types and the associated actions.
#        Check to see if the role exists before trying to add ACL rules.

from mixcoatl.admin.account import Account
from mixcoatl.admin.group import Group
from mixcoatl.admin.role import Role
from mixcoatl.admin.user import User
from prettytable import PrettyTable
import argparse
from argparse import ArgumentParser
import pprint
import esid
import resource_filter
import sys,os
import json

def validate_input(update_file):
    """
    This method validates the input file. Returns true if the JSON is valid, false
    otherwise.
    """
    try:
        json.load(open(update_file))
        print "Valid JSON"
        return True
    except ValueError:
        print "Invalid JSON"
        exit(-1)
        return False

def is_valid_file(parser, arg):
    """Check to see if the file passed to -i is in fact a file. If it is, check to see if
       it's a valid json format."""
    if not os.path.isfile(arg):
       parser.error("The file %s does not seem to be a file at all! Exiting for safety reasons." %arg)
       sys.exit(1)
    else:
       if validate_input(arg):
           return True
       else:
           print "Invalid JSON. Exiting"
           sys.exit(1)

def update_acl_from_file(role_id):
    """Loop through the contents of the ACL file and add the specified ACL."""
    r=Role(role_id)
    parser = ArgumentParser(description="role ACL json")
    if is_valid_file(parser,filename):
        f=open(filename,'r')
        json_object = json.load(f)
        print json_object

    for value in json_object.values():
        for v in range(0,len(value)):
            r.grant(role_id, value[v]['resourceType'], value[v]['action'], value[v]['qualifier'])

def update_acl(role_id,resource,action,qualifier):
    """Add this single rule."""
    r=Role(role_id)

    result = r.grant(role_id,resource,action,qualifier)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--role_id', '-r', type=int, help='The role ID.')
    parser.add_argument('--action', '-a', help='ACL action')
    parser.add_argument('--resource', '-R', help='ACL resource')
    parser.add_argument('--qualifier', '-q', help='ACL qualifier')
    parser.add_argument("-i", dest="filename", required=False,
        help="input file for setting role ACL", metavar="FILE")

    cmd_args = parser.parse_args()

    role_id=cmd_args.role_id
    resource=cmd_args.resource
    action=cmd_args.action
    qualifier=cmd_args.qualifier
    filename=cmd_args.filename

    # Load from file specified by -i
    if cmd_args.filename and cmd_args.role_id:
        update_acl_from_file(role_id)
        sys.exit(0)

    if (cmd_args.role_id is None or cmd_args.action is None or cmd_args.resource is None or cmd_args.qualifier is None):
        parser.print_help()
        sys.exit(1)
    else:
        update_acl(role_id,resource,action,qualifier)