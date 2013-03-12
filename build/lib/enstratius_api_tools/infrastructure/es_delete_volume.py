#!/usr/bin/env python
# This script doesn't work since mixcoatl's destroy function hasn't been implemented yet.

from mixcoatl.infrastructure.volume import Volume
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('volumeid', type=int, help='Volume ID')
    parser.add_argument('--reason', '-r', help='The reason for deleting the volume.')

    cmd_args = parser.parse_args()

    volume = Volume(cmd_args.volumeid)
    result = volume.destroy(cmd_args.reason)

    if result is True:
        print("Deleting the volume.")
    else:
        print("Failed to delete the volume.")
        sys.exit(1)
