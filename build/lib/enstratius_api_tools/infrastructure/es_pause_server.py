#!/usr/bin/env python

from mixcoatl.infrastructure.server import Server
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('serverid', type=int, help='Server ID')

    cmd_args = parser.parse_args()

    server = Server(cmd_args.serverid)
    result = server.pause()

    if result is True:
        print("Pausing the server.")
    else:
        print("Failed to pause the server.")
        sys.exit(1)