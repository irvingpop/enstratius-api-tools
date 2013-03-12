#!/usr/bin/env python

from mixcoatl.admin.job import Job
from prettytable import PrettyTable
import argparse
import sys

if __name__ == '__main__':
    """ Returns a list of jobs. """
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', help='Produce verbose output', action="store_true")
    cmd_args = parser.parse_args()

    all_jobs = Job.all()

    if cmd_args.verbose:
        for job in all_jobs:
            job.pprint()
    else:
        job_table = PrettyTable(["Description", "Job ID", "Status", "Start Date", "End Date", "Message"])
        job_table.align['Description'] = 'l'

        for job in all_jobs:
            if hasattr(job, 'end_date'):
                end_date = job.end_date
            else:
                end_date = None
            if hasattr(job, 'message'):
                message = job.message
            else:
                message = None
            job_table.add_row([job.description, job.job_id, job.status, job.start_date, end_date, message])

        print(job_table)
