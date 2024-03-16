#!/usr/bin/python3
# Upload to web servers
from fabric.api import put, run, env
import os.path

env.hosts = ['35.175.134.192', '34.207.63.125']

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    f_name = os.path.basename(archive_path).split('.')[0]

    if put(archive_path, '/tmp').failed:
        return False
    if run('mkdir -p /data/web_static/releases/{}'.format(f_name)).failed:
        return False
    if run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
            f_name, f_name)).failed:
        return False
    if run('rm /tmp/{}.tgz'.format(f_name)).failed:
        return False
    if run('rm -f /data/web_static/current').failed:
        return False
    if run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(
            f_name)).failed:
        return False

    return True
