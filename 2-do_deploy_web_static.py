#!/usr/bin/python3
"""Upload to web servers"""


from fabric.api import put, run, env
import os.path

env.hosts = ['477100-web-01', '477100-web-02']


def do_deploy(archive_path):
    """Deploy on 2 webservers.

    Args:
        archive_path: path to archived file
    Returns:
        True if no errors, False if error or file doesnot exist
    """
    if not os.path.isfile(archive_path):
        return False

    name_of_file = os.path.basename(archive_path).split('.')[0]

    if put(archive_path, '/tmp').failed:
        return False
    if (run('mkdir -p /data/web_static/releases/{}'.format(
            name_of_file)).failed):
        return False
    if (run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
            name_of_file, name_of_file)).failed):
        return False
    if run('rm /tmp/{}.tgz'.format(name_of_file)).failed:
        return False
    if run('rm -f /data/web_static/current').failed:
        return False
    if (run('ln -s /data/web_static/releases/{}'.format(
            name_of_file) '/data/web_static/current').failed):
        return False

    return True
