#!/usr/bin/python3
""" Upload to web servers """


from fabric.api import put, run, env
import os.path

env.hosts = ['477100-web-01', '477100-web-02']


def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False
    put(archive_path, '/tmp')
    name_of_file = os.path.basename(archive_path).split('.')[0]
    run('mkdir -p /data/web_static/releases/{}'.format(name_of_file))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
        name_of_file, name_of_file))
    run('rm /tmp/{}.tgz'.format(name_of_file))
    run('rm -f /data/web_static/current')
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(
        name_of_file))
    return True
