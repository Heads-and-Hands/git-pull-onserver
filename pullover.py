#!/usr/bin/env python
import sys, getopt

from flask import Flask
from flask import request

import subprocess

from config import repos


def main(argv):
    try:
      opts, args = getopt.getopt(argv,"hr")
    except getopt.GetoptError:
      print_help()
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-r':
        run_service()
      elif opt == '-h':
        print_help()
        sys.exit(2)


def print_help():
    print '-r - Run service'


def run_service():
    print 'Runnin service...'
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        repo_id = request.args.get('key')
        current_repo = repos.get(repo_id)
        remote_name = current_repo.get('remote_name')
        remote_branch = current_repo.get('remote_branch')
        local_dir = current_repo.get('local_dir')
        cmd = ["cd %s && git reset --hard && git pull %s %s" % (local_dir, remote_name, remote_branch),""]
        p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        out,err = p.communicate()
        return out

    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main(sys.argv[1:])
#    app.run(host='0.0.0.0')

