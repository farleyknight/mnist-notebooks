# TODO:
#
# 0) Use `__import__` to `import`` using a string
#
# 1) Open file, for read-only. Store all data in a config/dict.
#
# 2) Open file again, this time in write-only. As we run the
# jobs, we change the status (new / in_progress / done / error)
#
# 3) Each job runs inside a try / except block. This allows us to mark
# jobs as 'error' if they threw an exception.
#
# 4) Add a verify step. This verifies that the function completed
# successfully. This could be a 5th state (rejected, if it did not
# pass the verify step) on jobs.
#
#

import json


def run_job(fn, args, verify):
    try:
        output = fn(args)
        if verify(args, output):
            return 'done'
        else:
            return 'rejected'
    except:
        return 'error'


def update_job_data(name, job_data):
    with open(f'jobs/{name}.json', 'w') as f:
        f.write(json.dumps(job_data, indent=4))


def run_jobs(args):
    name = args.name

    with open(f'jobs/{name}.json') as f:
        job_data = json.loads(f.read())

    description = job_data['description']
    print(f"Loading job data for {description}")

    fn_name = job_data['function']
    verify_fn_name = job_data['verify']

    module_to_import = job_data['import']
    module = __import__(module_to_import)
    function = getattr(module, fn_name)
    verify_fn = getattr(module, verify_fn_name)

    # TODO: Figure out how to parallelize this
    size = len(job_data['jobs'])
    print(f"Found {size} jobs to run")
    for job in job_data['jobs']:
        print('Found job with args', job['args'])
        if job['status'] != 'new':
            print('This job has already been started!')
            print('It has status', job['status'])
            print('Moving on to the next')
            continue

        # Mark the job as in_progress
        job['status'] = 'in_progress'
        update_job_data(name, job_data)

        # Run the job, update the status
        new_status = run_job(function, job['args'], verify_fn)
        print('New status: ', new_status)
        job['status'] = new_status
        update_job_data(name, job_data)


def main():
    import argparse

    argparser = argparse.ArgumentParser(
        description='Run Jobs from JSON config')
    argparser.add_argument(
        '--name', type=str, default='test_job_system', help='name of the JSON config to use')

    args = argparser.parse_args()
    run_jobs(args)


if __name__ == '__main__':
    main()
