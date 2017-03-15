import subprocess


def print_rfw_distro_version():
    process = subprocess.Popen(["lsb_release", "-a"], shell=False,
    						   stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out = process.communicate()
    print("RFW distro version: {}".format(out))
    	