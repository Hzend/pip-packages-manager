# coding: utf-8

import os
import json
import sys

def get_packages_info(args):
    if args == None:
        package_json = os.popen("pipdeptree --json-tree").read()
        package_json = json.loads(package_json)
        packages_info = package_json

        for packages in packages_info:
            package_name = packages.get("package_name")
            package_version = packages.get("installed_version")
            print(f"{package_name}=={package_version}")
    else:
        print('usage: python3 pip-packages-manager.py >> your_requirements.txt')

if __name__ == "__main__":
   get_packages_info(sys[1:])

