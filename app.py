from flask import Flask
import subprocess
from config import repos

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    current_repo = repos.get('key')
    remote_name = current_repo('remote_name')
    remote_branch = current_repo('remote_branch')
    local_dir = current_repo('local_dir')
    cmd = ["cd %s && git reset --hard && git pull %s %s" % (local_dir, remote_name, remote_branch),""]
    p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == "__main__":
    app.run(host='0.0.0.0')

