#!/usr/bin/env python
import logging, time, os, subprocess


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='../logs/fab.log',
                    filemode='a')


if __name__ == '__main__':
    if os.environ.get('ENABLE_DEBUG'):
        subprocess.check_call(['pip','install','django-debug-toolbar'])
    if 'LAUNCH_SERVER' in os.environ or 'LAUNCH_SERVER_NGINX' in os.environ:
        subprocess.check_call(['./migrate.sh',])
        subprocess.check_call(['./init_fs.py', ])
        subprocess.check_call(['./launch_from_env.py','0'])
    else:
        time.sleep(30)  # To avoid race condition where worker starts before migration is finished
        subprocess.check_call(['./init_fs.py', ])
        subprocess.check_call(['./launch_from_env.py','1'])