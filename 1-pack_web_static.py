#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
    from the contents of the web_static
"""


from Fabric import Connection
import os.path
from datetime import datetime


def do_pack():
    date = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year, date.month, date.day, date.hour, date.minute,
            date.second)
    if (os.path.isdir('versions') is False):
        if (local('mkdir -p versions').failed is True):
            return None
    if local('tar -cvzf {} web_static'.format(file_name)).failed is True:
        return None
    return file_name
