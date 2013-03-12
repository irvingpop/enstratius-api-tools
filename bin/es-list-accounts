#!/usr/bin/env python

from mixcoatl.admin.account import Account
from prettytable import PrettyTable
import esid
import argparse
import sys

def returnId(account):
    print "%-15d %-30s" % (account.account_id, account.name)

if __name__ == '__main__':
    """ List accounts. Right now just returns the ID and name of the account"""
    parser = argparse.ArgumentParser()

    a=Account().all()

    # This is expensive as hell, but it's the only way to get a list of accounts right now
    # if you're using a system/customer API key.

    numAccount=len(a)

    print "%-15s %-30s" % ('Account ID', 'Account Name')
    for index, object in enumerate(a):
        returnId(object)
