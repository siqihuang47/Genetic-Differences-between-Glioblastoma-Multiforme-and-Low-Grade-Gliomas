import subprocess

def get_data():
    subprocess.call("/src/download_data.R", shell=True)
