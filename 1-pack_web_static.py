#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
    from the contents of the web_static
"""


from fabric.api import local
import os.path
from datetime import datetime


def do_pack():
    """ function to archive web static file """
    date = datetime.utcnow()
    file_name = "versions/web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
            date.year, date.month, date.day, date.hour, date.minute,
            date.second)
    if (os.path.isdir('versions') is False):
        if (local('mkdir -p versions').failed is True):
            return None
    if local('tar -cvzf {} web_static'.format(file_name)).failed is True:
        return None
    return file_name
