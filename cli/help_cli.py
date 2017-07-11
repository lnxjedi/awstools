def processCommand(mgr, args):
    print("""
The 'maws' tool is a command line interface to the python-awstools configured
library for managing ephemeral AWS resources like instances, DNS records,
RDS instances, and CloudWatch alarms. Most operations are a complex combination
of AWS functions; for instance, creating an ec2 instance will also create a
DNS record and store metadata in SimpleDB.

Common options:
-c, --config <filename>     Use <filename> for the configuration file
                            (default 'cloudconfig.yaml')

Commands:

ec2         Manage ec2 instances

cfn         Manage cloudformation templates

rds         Manage RDS instances

route53     Manage DNS entries

sdb         Manage SimpleDB entries""")
