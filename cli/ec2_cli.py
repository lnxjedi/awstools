import argparse

def processCommand(mgr, args):
    parser = argparse.ArgumentParser(usage='''maws ec2 <subcommand> [<args>]
    maws ec2 help''')
    parser.add_argument('subcommand', help='ec2 subcommand',
        choices=[ 'help', 'create' ])
    args = parser.parse_args(args)

    if args.subcommand == "help":
        print("""
The 'ec2' subcommand performs high-level operations on ec2 instances. Each
command will update DNS entries and SimpleDB items as needed.

Sub-commands:

create <name>   Run a new instance for the first time

launch <name>   Run an instance that has been previously created and terminated

rebuild <name>  Terminate and re-launch and instance

start <name>    Restart a stopped instance

stop <name>     Stop a running instance

reconcile       Update SimpleDB tables from the running environment, useful
                for bootstrapping or updating after manual operations""")
