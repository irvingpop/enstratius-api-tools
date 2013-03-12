#!/usr/bin/env python

from mixcoatl.infrastructure.volume import Volume
import esid
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--budgetid', '-b', type=int, help='Budget ID.')
    parser.add_argument('--budgetname', '-B', help='Budget name.')
    parser.add_argument('--datacenter', '-d', type=int, help='Data Center ID in which to create the volume.')
    parser.add_argument('--description', '-D', help='The description of the volume.')
    parser.add_argument('--name', '-n', help='The name of the volume.')
    parser.add_argument('--size', '-s', type=int, help="The size of the volume in GB.")

    cmd_args = parser.parse_args()

    if ((cmd_args.budgetid is None and cmd_args.budgetname is None) or cmd_args.datacenter is None or
        cmd_args.description is None or cmd_args.name is None or cmd_args.size is None):
        parser.print_help()
        sys.exit(1)

    new_volume = Volume()

    new_volume.data_center = cmd_args.datacenter
    new_volume.description = cmd_args.description
    new_volume.name = cmd_args.name
    new_volume.size_in_gb = cmd_args.size

    if cmd_args.budgetid is not None:
        new_volume.budget = cmd_args.budgetid
    else:
        new_volume.budget = esid.get_budget_id(cmd_args.budgetname)

    result = new_volume.create()

    if result.status == 'RUNNING':
        print("Creating the volume. Job ID: %s" % result.job_id)
    else:
        print("Failed to create the volume.")
        sys.exit(1)
