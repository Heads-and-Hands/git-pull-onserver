from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    remote_name = 'origin'
    remote_branch = 'develop'
    cmd = ["git reset --hard && git pull %s %s" % (remote_name, remote_branch),""]
    p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == "__main__":
    app.run(host='0.0.0.0')

