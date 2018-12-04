======
README
======

***********************
Burst Buffer Check Tool
***********************

This tool is designed to make the process of understanding diagnostic
information about the status of a Cray system's burst buffer facility less time
consuming.  It cross-correlates information gathered from the system-provided
`dwstat` tool to display information about burst buffer nodes and sessions in an
easy-to-read, color-coded, hierarchical format.

The tool was designed for Python 2 and requires Python 2.7 or above. 

|


Configuration
=============

This tool can be installed by a user with write access to /etc. During install,
you will be asked some questions about naming conventions on your system and
asked to provide further information about a user that has necessary permissions
to run the program. After installation, configuration can be changed by editing
the /etc/bbcheck.cfg file.  For more information about what answers the install
questions need or how to edit the configuration file, see the section titled
"Configuration Settings"

If you choose not to install, you can still use the tool. Simply place the files
`bbcheck` and `bbconfig.py` in the same directory and edit bbconfig.py below the
commented line with your configuration settings. The `demo_strings.py` files is
not required unless you wish to use the `--testing` flag for demonstration
purposes. You can then run the tool with `./bbcheck`.

This tool can be run on either the boot node, or on the SMW node.
Ideally, a user should be available that has keyed and passwordless ssh
authorization to the boot node.

|

Configuration Settings
======================

- DW_NODE_PREFIX : The prefix used in the numerical naming of your system's burst buffer nodes. For example, in the default configuration where the 214th burst buffer node is `bb214` the prefix would be "bb".
- DWSTAT_PATH : The path of the Cray `dwstat` tool on the boot node.
- BOOT_NODE_NAME : The name of the boot node.  The default is `boot`.
- DWSTAT_AUTHORIZED_USER : The username of of a user that has permission to ssh into the boot node (if running the tool on the SMW) and to run `dwstat`.
- SMW_HOSTNAME : The hostname of your system's SMW node.

Running The Tool
================



Running `bbcheck` without any options will show you information about datawarp sessions and nodes in bad states. The other following options are available:

- `-a` : Will show all sessions
- `-c` : Will show a filtered version of the `dwstat` output, rather than the normal hierarchical view
- `-m` : Will display in monochrome (useful for scripting, or dumping output to a file)
- `--testing` : Displays a demo
