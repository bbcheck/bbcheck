#!/usr/bin/env python
"""
Setup script for BBcheck
"""

from __future__ import print_function
from distutils.core import setup

try:
    open("/etc/bbcheck.cfg", "w").close()
except IOError:
    print("You must have write permissions to /etc to install this progam\n"+
          "for instructions on using this program without installing, please "+
          "see README.rst\n")
    exit()

def create_config_file():
    """
    Creates config file based on user's answers to questions
    """
    print("Welcome to the BBcheck installation tool. Please answer a " +
          "few short questions to configure BBcheck for your system. " +
          "Further information about these questions is available in " +
          "README.rst. You can always change this information later in " +
          "/etc/bbcheck.cfg\n")
    config_vars = {}
    config_vars["dw_node_prefix"] = raw_input("Please enter the naming prefix for your system's " +
                                              "burst buffer nodes : ").strip()
    print()
    config_vars["boot_node_name"] = raw_input("Please enter the hostname of your boot node" +
                                              " : ").strip()
    print()
    config_vars["smw_hostname"] = raw_input("Please enter the hostname of your SMW node : ").strip()
    print()
    config_vars["dwstat_path"] = raw_input("Please enter the absolute path of the dwstat " +
                                           "executable on %s : " %
                                           config_vars["boot_node_name"]).strip()
    print()
    config_vars["dwstat_authorized_user"] = raw_input("Please enter the username of a user that " +
                                                      "is authorized to ssh in the boot node " +
                                                      " from the SMW node and can run the " +
                                                      " dwstat executable : ").strip()
    with open("/etc/bbcheck.cfg", "w") as cfg_file:
        cfg_file.write("[bbcheck]\n")
        for key, value in config_vars.items():
            cfg_file.write("%s=%s\n" % (key, value))

create_config_file()
setup(name="BBcheck",
      version='1.0',
      description="Tool for rapidly identifying Datawarp issues",
      author="John Gann",
      author_email='jgann@lbl.gov',
      packages=['bbcheck'],
      scripts=['bbcheck/bbcheck']
     )
