"""The maws manager module provides classes and functions used for dealing with
configuration, parameters, and templates.
"""

class Manager:
    """Central utility class

    Provides methods for accessing configuration, parameters, and template
    expansion."""

    def __init__(self, filename):
        """Read and store the config file

        Args:
            filename (str): name of yaml file relative to current dir
                            (project root)
        """
        self.configfile = filename

    def showname(self):
        """Throw-away method for initial testing"""
        print("Config file is: %s" % self.configfile)
