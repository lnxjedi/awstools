# AWSTools
AWS Tools is a configurable library for integrated management of AWS ephemeral resources.
Instead of each volume / ec2 instance / rds instance / whatever being defined in a list of
resources, AWS Tools focuses on a higher-level abstraction layer for dynamically creating,
starting, stopping, etc. resources.

## Status
`awstools` is an in-progress re-write of 'ruby-awstools', with as yet no usable functionality.

## Intent
The intent is to create a tool that uses the AWS API to manage individual server instances,
essentially implementing a flexible data center in the Cloud. The intial driver was for
managing inexpensive single web servers for users and departments at the University of
Virginia, where users expect a traditional server where the website is under /var/www/html,
their home directory has content and scripts that is preserved during patching, etc.

This library simplifies the process of launching servers with integrated DNS updates, and
gives simple methods that allow for patching, cloning, backing up and restoring servers.

## Audience

### Who this tool is for
This tool is designed for Systems Engineers supporting a wide range of users of varying
technical competency. It primarily focuses on functionality provided by AWS IAAS for
supporting traditional workloads.

### Who this tool is not for
This tool is not intended to provide any further functionality on top of AWS-specific
PAAS and SAAS services such as Elastic Beanstalk.

## Design Principals
* All operations are logged to CloudWatch logs with information about the user who
intiated the operation
* Resources are created based on a library-standard and flexible template format that
the library processes to create e.g. CloudFormation templates or API option data
structures
* The bulk of code should be in a loadable library, with the provided CLI being a
lightweight user interface to the library
* The library should be readily loadable and useable by other scripts
* Methods are intended to be useful for workflows like:
  * Patching servers
  * Cloning servers
  * Transitioning servers through devel/test/staging/production
* The tool operates on configuration files in a separate data repository, similar
to Ansible
