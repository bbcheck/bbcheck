"""
This module provides configuration information for bbcheck,
either by reading a config file, or have the values set directly
"""

import os
import os.path
import ConfigParser

CONFIG_FILE_PATH = "/etc/bbcheck.cfg"

if os.path.isfile(CONFIG_FILE_PATH):
    config = ConfigParser.RawConfigParser()
    with open(CONFIG_FILE_PATH) as cfg_file:
        config.readfp(cfg_file)
        DW_NODE_PREFIX = config.get("bbcheck", "dw_node_prefix")
        DWSTAT_PATH = config.get("bbcheck", "dwstat_path")
        BOOT_NODE_NAME = config.get("bbcheck", "boot_node_name")
        DWSTAT_AUTHORIZED_USER = config.get("bbcheck", "dwstat_authorized_user")
        SMW_HOSTNAME = config.get("bbcheck", "smw_hostname")
else:
    #If running without installing, configure using the values below
    DW_NODE_PREFIX = "bb"
    DWSTAT_PATH = "/opt/cray/dws/default/bin/dwstat"
    BOOT_NODE_NAME = "boot"
    DWSTAT_AUTHORIZED_USER = "root"
    SMW_HOSTNAME = "corismw"
