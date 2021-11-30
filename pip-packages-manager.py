# coding: utf-8

import os
import json
import sys, getopt

def get_file_name(argv):

    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print('usage: python3 test.py -o requirements.txt')
      sys.exit(2)
    for opt, arg in opts:
      if opt == "-o":
         return arg
      else:
          print('usage: python3 test.py -o requirements.txt')
          sys.exit()

def get_packages_info(file_name):
    os.environ["PATH"] = "/home/project/pip-package-manager/bin"

    package_json = os.popen("pipdeptree --json-tree").read()
    package_json = json.loads(package_json)
    packages_info = package_json

    for packages in packages_info:
        package_name = packages.get("package_name")
        package_version = packages.get("installed_version")
        with open(file_name, "a") as f:
            f.write(f"{package_name}=={package_version}\n")


def main():
    file_name = get_file_name(sys.argv[1:])
    get_packages_info(file_name)

if __name__ == "__main__":
   main()

