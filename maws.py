#!/usr/bin/python3

import argparse
import sys
from mawslib.manager import Manager
import importlib

configfile="cloudconfig.yaml"

parser = argparse.ArgumentParser(
    #add_help=False,
    description='AWS Manager',
    usage='''maws [<options>] <command> <subcommand> [<args>]

For help:
   maws help
   maws <command> help
   maws <command> <subcommand> help
''')
parser.add_argument('command', help='Command to run',
    choices = ['help', 'ec2', 'sdb', 'route53', 'r53', 'rds',
    'cloudformation', 'cfn' ])
parser.add_argument('--config',
    help='alternate config file to use (default: cloudconfig.yaml)',
    action="store")
# parse_args defaults to [1:] for args, but you need to
# exclude the rest of the args too, or validation will fail
args, subargs = parser.parse_known_args()

if hasattr(args, "config"): configfile = args.config
mgr = Manager(configfile)
mgr.showname()

if args.command == "cfn": args.command = "cloudformation"
if args.command == "r53": args.command = "route53"

cli_mod = importlib.import_module("cli.%s_cli" % args.command)
cli_mod.processCommand(mgr, subargs)
