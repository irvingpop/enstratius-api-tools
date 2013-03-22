#!/usr/bin/env python

from mixcoatl.infrastructure.server import Server
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('serverid', type=int, help='Server ID')
    parser.add_argument('--reason', '-r', help='The reason for terminating the server.')

    cmd_args = parser.parse_args()

    server = Server(cmd_args.serverid)
    result = server.destroy(reason=cmd_args.reason)

    if result is True:
        print("Terminating the server.")
    else:
        print("Failed to terminate the server.")
        sys.exit(1)