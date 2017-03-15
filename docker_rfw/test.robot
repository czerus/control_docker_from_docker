*** Settings ***
Library    Remote    http://127.0.0.1:8270
Library    /rfw/locallib.py

*** Test Cases ***
Print test distro version
    print_test_distro_version

Print rfw distro version
    print_rfw_distro_version

Restart Tomcat
    kill_tomcat
