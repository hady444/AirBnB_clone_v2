#!/usr/bin/python3
# Full deployment


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """ Full deployment """
    archive_file = do_pack()
    if archive_file is None:
        return False
    return do_deploy(archive_file)
