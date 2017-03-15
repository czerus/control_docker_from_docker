import subprocess


class MyRemoteLib(object):
    def print_test_distro_version(self):
        process = subprocess.Popen(["lsb_release", "-a"], shell=False,
                               stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out = process.communicate()
        print("TEST distro version: {}".format(out))

    def kill_tomcat(self):
        process = subprocess.Popen(["pkill", "java"], shell=False,
                                   stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = process.communicate()
        if not err:
            print("Tomcat server killed.")
        else:
            print("Some error occured.")


if __name__ == '__main__':
    import sys
    from robotremoteserver import RobotRemoteServer

    RobotRemoteServer(MyRemoteLib(), *sys.argv[1:])
