import subprocess

def get_data():
    subprocess.call("download_data.R", shell=True)
